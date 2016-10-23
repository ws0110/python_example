# coding: utf-8

'''
  웹크롤러 전체 소스
'''

import urllib.robotparser
import urllib.request
import time, traceback, re, sys, os
import database
from bs4 import BeautifulSoup

# 상수
CRAWLER_NAME = 'python_daum_crawler'
MAINPAGE = 'http://blog.daum.net/'
MAINPATH = './data/'


# DB
db = database.DB()

# robot parser 설정
rp = urllib.robotparser.RobotFileParser(MAINPAGE + 'robots.txt')
rp.read()

def canFetch(url):
    'URL 수집여부 가능한지 확인'
    return rp.can_fetch(CRAWLER_NAME, url)


def getContent(url, delay=1):
    '웹페이지 내용 조회'
    time.sleep(delay)
    if not canFetch(url):
        print('This url can NOT be fetched by our crawler :', url)
        return None

    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', CRAWLER_NAME)]
        contents = opener.open(url).read()
        #print(contents)
    except:
        traceback.print_exc()  ## 에러스택 정보를 stdout으로 print
        return None
    return contents


def getArticleInfo(soup):
    '블로그내의 articla info 조회'
    rBlog = re.compile(r'.+blog.daum.net/\w+\d+.*?')
    #print(rBlog.findall('http://blog.daum.net/simhsook48?t__nil_recomm=vipimg'))
    URLs = soup.find_all('a', attrs={'href':rBlog})
    return [u['href'].split('?')[0] for u in URLs]


def parseArticle(url):
    'url을 파싱하고 저장'
    blog_id = url.split('/')[-1]

    # redirect된 주소 얻기
    newUrl = getRedirectedURL(url)
    if newUrl:
        try:
            # blog 디렉토리 생성
            path = MAINPATH + blog_id
            if not os.path.exists(path):
                os.makedirs(path)
        except:
            traceback.print_exc()
            pass # 무시

        newUrl = 'http://blog.daum.net' + newUrl
        print('newUrl: ', newUrl)
        contents = getContent(newUrl, 0)
        if not contents:
            print('Null Contents...')
            db.updateURL(url, -1)  # 유효하지 않은 url은 -1 저장
            return

        # html 파싱
        soup = BeautifulSoup(contents, "html.parser")

        # 이웃 블로거 정보가 있는지 확인
        gatherNeighborInfo(soup)

        # 블로그 url이 있는 경우 db insert
        n = 0
        for u in getArticleInfo(soup):
            n += db.insertURL(u)
        if n>0:
            print('inserted %d urls from %s' % (n, url))

        # title 얻기
        sp = contents.find(r'<title>')
        if sp > -1:
            ep = contents[sp+7:].find(r'</title>')
            title = contents[sp+7:sp+7+ep]
        else:
            title = ''

        # 본문 HTML 정리
        contents = getBody(soup, newUrl)

        # script들 제거
        pStyle = re.compile(r'<style(.*?)>(.*?)</style>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
        contents =  pStyle.sub('', contents)
        pStyle = re.compile(r'<script(.*?)>(.*?)</script>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
        contents = pStyle.sub('', contents)
        pStyle = re.compile(r'<(.*?)>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
        contents = pStyle.sub('', contents)

        #txt file 저장
        fTxt = open(MAINPATH + blog_id + '.txt', 'w')
        fTxt.write(title + '\n')  # 제목을 첫줄에
        fTxt.write(contents)
        fTxt.close()
        db.updateURL(url) # 처리완료 DB 저장

    else:
        print('Invalid blog article...')
        # 유효하지 않은 url -1로 DB 저장
        db.updateURL(url, -1)




def getBody(soup, parent):
    '본문 텍스트 조회'

    #본문 주소를 포함하는 iframe 찾기
    rSrc = re.compile(r'.+/ArticleContentsView.+')
    iframe = soup.find_all('iframe', attrs={'src':rSrc})
    if len(iframe)>0:
        src = iframe[0].get('src')
        iframe_src = 'http://blog.daum.net' + src

        # 그냥 request가 아닌, referer 지정(browser를 통해서 request한 것으로 인식시킴)
        req = urllib.request.Request(iframe_src)
        req.add_header('Referer', parent)
        body = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(body, "html.parser")
        return str(soup['body'])
    else:
        print('Null contents')
        return ''

def gatherNeighborInfo(soup):
    '이웃 블로거 or 다녀간 블로거 정보 수집'

    rBlog = re.compile(r'http://blog.daum.net/\w+')
    Neighbors = soup.find_all('a', attrs={'href':rBlog})

    cnt = 0
    for n in Neighbors:
        url = n['href']
        blogId = url.split('/')[-1]
        if url and url.startswith('http://') and db.isCrawledURL(url)<1:
            db.insertURL(url, 1) # 읽은것으로 저장

            url2 = getRedirectedURL(url) # Redirect된 URL조회
            if not url2: continue
            re_url = 'http://blog.daum.net' + url2
            body = getContent(re_url, 0) # frame내의 문서 읽기
            if body:
                for articleId in getOwnArticles(body):
                    # 자신의 글 주소들을 DB에 저장
                    fullpath = 'http://blog.daum.net/' + blogId + '/' + articleId
                    cnt += db.insertURL(fullpath)
    if cnt>0:
        print('%d neighbor articles inserted' % cnt)

def getOwnArticles(contents):
    '해당 블로그의 글 리스트 조회'
    ret = []
    soup = BeautifulSoup(contents, "html.parser")
    rBlog = re.compile(r'.+/BlogView.+')
    for u in soup.find_all('a', attrs={'href':rBlog}):
        href = u['href']
        article = href.split('articleno=')[1].split('&')[0]
        if ret.count(article) <1:
            ret.append(article)
    return ret

def getRedirectedURL(url):
    '본문에 해당하는 frame의 url 조회'
    contents = getContent(url)
    if not contents:
        return None

    #redirect
    try:
        soup = BeautifulSoup(contents, "html.parser")
        frame = soup('frame')
        src = frame[0].get('src')
    except:
        src = None
    return src


if __name__ == '__main__':
    print('strting crawling...')

    #메인 페이지 체크
    contents = getContent(MAINPAGE)
    URLs = getArticleInfo(BeautifulSoup(contents, "html.parser"))
    print(URLs)


    nSuccess = 0
    for u in URLs:
        nSuccess += db.insertURL(u) # 메인페이지 URL 등록
    print('inserted %d new pages.' % nSuccess)

    while True:
        for u in db.selectUncrawledURL():
            # 읽지 않은 URL 처리
            print('downloading %s' % u)
            try:
                parseArticle(u)
            except:
                traceback.print_exc()
                db.updateURL(u, -1)






#database.DB()
#contents = getContent('http://blog.daum.net')
#soup = BeautifulSoup(contents, "html.parser")
#print(soup('a'))