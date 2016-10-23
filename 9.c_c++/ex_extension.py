# coding: utf-8

import spam

### 'spammodule.c' 확장 테스트
print(spam.strlen('abc'))
print(spam.division(10,2))


##### 참조 카운트
'''
메모리 참조(Reference) 카운트는 파이썬에서는 자동관리 됨
C확장 모듈에서는 사용자가 참조 카운트를 직접 증가/감소 관리해줘야 함
 => Py_INCREF(), Py_DECREF(), Py_XINCREF(), Py_XDECREF() 함수 사용

* 참조 소유권 법칙
  1. PyLong_FromLong(), Py_BuildValue() : 참조 소유권을 같이 넘겨 줌(소유권 유지하고 싶은면 Py_INCREF() 실행 필요)
  2. PyTuple_GetItem(), PyList_GetItem(), PyDict_GetItem() : 참조만 넘겨줌
'''

###### C를 이용하여 파이썬의 새로운 타입(ex.리스트, 튜플 등)을 생성 가능


####### ctypes
'''
import ctypes
 - C의 데이터 타입이나, DLL 혹은 공유 라이브러리(shared library)의 함수를 직접 사용 가능
 - c_short, c_int, c_long, c_double, c_char_p 등 데이터 타입 바로 사용 가능
'''
import os
import ctypes
print(os.getcwd())
libtest = ctypes.cdll.LoadLibrary(os.getcwd() + '/ctypes_source.so')
print(libtest.multiply(2, 2))

i = ctypes.c_int(10)
print('cytpes: ', i, ', value: ', i.value)

pk = ctypes.pointer(i)   ## 포인터 지원
print('position: ', pk, ', cytpes: ', pk.contents, ', value: ', pk.contents.value)
