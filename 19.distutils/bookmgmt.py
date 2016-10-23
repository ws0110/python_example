# coding: utf-8

'''
  파이썬 내장 모듈만을 활용한 '도서관리 프로그램'
  기타 편리한 외장모듈이 많음(실전에서 주로 사용)
'''

from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree


#### Global ####
loopFlag = 1
xmlFD = -1
BooksDoc = None

### 메뉴 ###
def printMenu():
    print('\nWelcome! Book Manager Program(xml version)')
    print('===== Menu =====')
    print('Load xml: l')
    print('Print dom to xml: p')
    print('Quit program: q')
    print('print Book list: b')
    print('Add new book: a')
    print('sEarch book title: e')
    print('Make html: m')
    print('================')


### 메뉴 선택 실행 ###
def launcherFunction(menu):
    global BooksDoc
    if menu == 'l':
        BooksDoc = loadXmlFromFile()
    elif menu == 'p':
        printDomToXml()
    elif menu == 'q':
        quitBookMgr()
    elif menu == 'b':
        printBookList(['title',])
    elif menu == 'a':
        addBook()
    elif menu == 'e':
        searchBookTitle()
    elif menu == 'm':
        makeHtmlDoc()
    else:
        print('error: unknow menu key')


### XML 파일 로딩 ###
def loadXmlFromFile():
    global xmlFD
    fileName = str(input('Input file name to load: '))

    try:
        xmlFD = open(fileName)
    except IOError:
        print('invalid file name or path')
        return None

    try:
        dom = parse(xmlFD)
    except Exception:
        print('fail loading!')
    else:
        print('XML loading complete')
        return dom

    return None


### XML 출력 ###
def printDomToXml():
    if checkDocument():
        print(BooksDoc.toxml())


### Book Title 출력 ###
def printBookList(tags):
    global BooksDoc
    if not checkDocument():
        return None

    booklist = BooksDoc.childNodes
    books = booklist[0].childNodes
    for item in books:
        if item.nodeName == 'book':
            subitem = item.childNodes
            for atom in subitem:
                if atom.nodeName in tags:
                    print('title=', atom.firstChild.nodeValue)


### ADD Book ###
def addBook():
    global BooksDoc
    isbn = str(input('insert ISBN: '))
    title = str(input('insert Title: '))

    if not checkDocument():
        return None

    newBook = BooksDoc.createElement('book')  # Book 엘리먼트 생성
    newBook.setAttribute('ISBN', isbn)  # attribute 설정
    titleEl = BooksDoc.createElement('title') # title 엘리먼트
    titleText = BooksDoc.createTextNode(title) # title Text

    try:
        titleEl.appendChild(titleText)
    except Exception:
        print('append fail!! - title')
        return None

    try:
        newBook.appendChild(titleEl)
    except Exception:
        print('append fail!! - newBook')
        return None

    booklist = BooksDoc.firstChild
    booklist.appendChild(newBook)


### Book Title 검색 ###
def searchBookTitle():
    global BooksDoc
    if not checkDocument():
        return None

    keyword = str(input('insert keyword: '))

    try:
        tree = ElementTree.fromstring(str(BooksDoc.toxml()))
    except Exception:
        print('Element Tree parsing Error')
        return None

    bookElements = tree.getiterator('book')  # book 엘리먼트 전체 가져옴
    for item in bookElements:
        strTitle = item.find('title')  # title 엘리먼트 가져옴
        #print('>>>>> ', type(strTitle))
        if strTitle.text.find(keyword) >= 0:
            print('title: ', strTitle.text)


### DOM 생성(HTML 생성) ###
def makeHtmlDoc():
    from xml.dom.minidom import getDOMImplementation
    global BooksDoc
    if not checkDocument():
        return None

    impl = getDOMImplementation()
    newdoc = impl.createDocument(None, 'html', None) # 최상위 엘리먼트 생성
    top_element = newdoc.documentElement  ## documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)
    body = newdoc.createElement('body')

    tree = ElementTree.fromstring(str(BooksDoc.toxml()))
    bookElements = tree.getiterator('book')  # book 엘리먼트 전체 가져옴
    for item in bookElements:
        b = newdoc.createElement('b')
        ibsnText = newdoc.createTextNode('ISBN: ' + item.attrib['ISBN'])
        b.appendChild(ibsnText)
        body.appendChild(b)

        br = newdoc.createElement('br')
        body.appendChild(br)

        p = newdoc.createElement('p')
        titleText = newdoc.createTextNode('Title: ' + item.find('title').text)
        p.appendChild(titleText)
        body.appendChild(p)

        body.appendChild(br)

    top_element.appendChild(body)
    print(newdoc.toxml())


### 프로그램 끄기 ###
def quitBookMgr():
    global loopFlag
    loopFlag = 0
    booksFree();

### DOM 메모리 해제 ###
def booksFree():
    if checkDocument():
        BooksDoc.unlink()



### DOM 체크 ###
def checkDocument():
    global BooksDoc
    if BooksDoc == None:
        print('Error: Document is empty')
        return False
    return True

#### RUN ####
while(loopFlag > 0):
    printMenu()
    menuKey = str(input('select menu: '))
    launcherFunction(menuKey)
else:
    print('Thank You! Good Bye')