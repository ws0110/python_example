# coding: utf-8

'''
  robotparser 모듈
    - robot exclusion protocol: 웹 사이트에 검색 로봇이 자료수집이 가능한지 어느 디렉토리에 접근가능한지 정의하는 규정
'''

import urllib.robotparser
rp = urllib.robotparser.RobotFileParser('http://blog.daum.net/robots.txt')
rp.read()
print(rp.can_fetch('mycrawler', 'http://blog.daum.net'))

rp2 = urllib.robotparser.RobotFileParser('http://section.blog.naver.com/robots.txt')
rp2.read()
print(rp2.can_fetch('mycrawler', 'http://section.blog.naver.com'))