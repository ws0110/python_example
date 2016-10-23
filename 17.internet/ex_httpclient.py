# coding: utf-8

'''
  http.client 모듈
    - Naver OpenApi를 사용한 테스트
'''

import http.client
from xml.etree import ElementTree

def getNaverBookInfo(isbn):

    conn = http.client.HTTPSConnection('openapi.naver.com')
    reqHeaders = {
        'X-Naver-Client-Id': '5_jOlHKslr0ThwSi9an6',
        'X-Naver-Client-Secret': 'soONNoFxrX'
    }
    conn.request('GET', '/v1/search/book_adv.xml?query=test&d_isbn=' + isbn, None, reqHeaders)
    res = conn.getresponse()
    print(res.status, res.reason) # 응답코드, 메시지

    print(res.getheaders()) # 응답 헤더
    cLen = res.getheader('Content-Length')
    result = res.read(cLen); # 응답 내용
    print(result)

    return result


def extractBookData(strXml):

    tree = ElementTree.fromstring(strXml)
    items = tree.getiterator('item')
    for item in items:
        isbn = item.find('isbn')
        title = item.find('title')
        print('isbn: ', isbn.text, '/ title: ', title.text)



strXml = getNaverBookInfo('0596513984')
extractBookData(strXml)


