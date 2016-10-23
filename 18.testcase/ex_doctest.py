# coding: utf-8

'''
  doctest 모듈
    - 주석에 있는 내용 테스트 실행 함
    - 실행: python3 ex_doctest.py -v (v 옵셥이 테스트결과 출력해줌)
'''

import doctest

def div(x, y):
    '''
    This function is to divide x into y

    >>> div(1,2)
    0.5

    '''
    return x/y

if __name__ == '__main__':
    doctest.testmod()