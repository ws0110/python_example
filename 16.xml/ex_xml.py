# coding: utf-8

'''
  xml.parsers.expat 모듈: 빠른 xml 파싱(Handler 기반 처리)
  xml.dom 모듈 (객체 기반 처리)
  xml.sax 모듈 (핸들러 기반 처리)
  xml.etree.ElementTree 모듈
'''

##################   xml.parsers.expat  ###############

import xml.parsers.expat

TEST_XML = '<?xml version="1.0" ?><book ISBN="1111"><title>Loving You</title></book>'


def start_element(name, attrbs):
    print('Start element: ', name, attrbs)

def char_data(data):
    print('CharData: ', data)

def xml_info(version, encoding, standalone):
    print('Xml Info: ', version, encoding, standalone)

pa = xml.parsers.expat.ParserCreate()
pa.StartElementHandler = start_element
pa.CharacterDataHandler = char_data
pa.XmlDeclHandler = xml_info
pa.Parse(TEST_XML)




##################  xml.dom ###############

import xml.dom.minidom

doc = xml.dom.minidom.parse('book.xml')
titles = doc.getElementsByTagName('title')  ## nodeList 리턴
print(titles, ', cnt: ',titles.length)
print(doc.toxml())
booklist = doc.childNodes
print(type(booklist), len(booklist), booklist[0])
book = booklist[0].childNodes
print(book, len(book), book[0])

print(doc.nodeName, doc.nodeType)

for bookitem in book:
    print('NodeType=', bookitem.nodeType, ', NodeName=', bookitem.nodeName)  ## nodeType, nodeName
    if bookitem.nodeType == 3:
        print('NodeValue=', bookitem.nodeValue)  ## nodeValue






