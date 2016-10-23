
####### range(): range(['시작값:0'], '종료값', ['증가값:1'])
print(list(range(10)))
print(list(range(5, 10)))
print(list(range(10, 0, -1)))
print(list(range(10, 20, 2)))


####### enumerate(): enumerate('객체', ['인덱스시작값:0'])   인덱스,Value 함께 조회
L = [10, 20, 30, 40]
for i in enumerate(L):
    print(i)
for i in enumerate(L, 100):
    print(i)


####### LIST 내장
I1 = (i ** 2 for i in range(5))
print(list(I1))

L1 = ['apple', 'banana', 'orange', 'kiwi']
I2 = (i for i in L1 if len(i) > 5)
print(list(I2))

L3 = [1, 2, 3]
L4 = [4, 5, 6]
I3 = (x*y for x in L3 for y in L4)
print(list(I3))


######## Filter 함수
def getBiggerThan20(i):
    return i > 20
L5 = [10, 25, 30]
I4 = filter(getBiggerThan20, L5)  # filter(lambda i: i > 20, L) 가능
print(list(I4))


########### ZIP
X = [10, 20, 30]
Y = ['A', 'B', 'C', 'D']  # D는 무시 됨
ret = list(zip(X, Y))
print(ret)
X2, Y2 = zip(*ret)  ## 풀기
print(X2, Y2)


###########  MAP
L6 = [1, 2, 3]
def add10(i):
    return i+10
I5 = (i for i in map(add10, L6))
print(list(I5))

L7 = [4, 5, 6]
I6 = (i for i in map(pow, L6, L7))  ## 매개변수 2개 이상
print(list(I6))


###########  FOR 성능
L8 = ['apple', 'banana', 'orange', 'kiwi']
print(', '.join(L8))   ### print문 단 한번 실행으로 for문 사용해서 print() 매번 실행하는것 보다 효율적!!

