# coding: utf-8

'''
모듈 사용 테스트
 1. 같은 디렉토리에 있으면 import 가능
 2. 환경변수 PYTHONPATH=모듈 디렉토리
 3. import sys
    sys.path.append('모듈 디렉토리')
'''

#from simpleset import *
import simpleset
print(dir(simpleset))

setA = [1, 3, 7, 10]
setB = [2, 3, 4, 9]
print(simpleset.intersect(setA, setB))
