# coding: utf-8

'''
 집합 관련 모듈
'''

from functools import *

def intersect(*ar):
    '교집합'
    return reduce(__intersectSC, ar)  ## reduce 함수: 매개변수를 누적적으로 함수 적용


def __intersectSC(listX, listY):
    setList = []
    for x in listX:
        if x in listY:
            setList.append(x)
    return setList


def union(*ar):
    '합집합'
    setList = []
    for item in ar:
        for x in item:
            if not x in setList:
                setList.append(x)
    return setList


def difference(*ar):
    '차집합'
    setList = []
    intersectSet = intersect(*ar)
    unionSet = union(*ar)
    for x in unionSet:
        if not x in intersectSet:
            setList.append(x)
    return setList


if __name__ == '__main__':
    print('module test!!')
    setA = [1, 3, 7, 10]
    setB = [2, 3, 4, 9]
    print(intersect(setA, setB))
    print(union(setA, setB))
    print(difference(setA, setB))
else:
    print('module imported!!')
