# coding: utf-8

'''
  sys 모듈
   : 파이썬 인터프리터 관련 정보 제공
'''

import sys

print(sys.argv)
for i, arg in enumerate(sys.argv):
    print(i, arg)

print(sys.prefix) # 파이썬 설치 경로
print(sys.exec_prefix)
print(sys.executable) # 파이썬 인터프리터 실행 파일 경로

t = 'test'
t1 = t
print(sys.getrefcount(t))  # 객체 참조 카운트

print(sys.path) # 모듈 참조 경로
print(sys.version)
print(sys.getdefaultencoding())
sys.stdout.write('hi')
sys.stderr.write('hi')


