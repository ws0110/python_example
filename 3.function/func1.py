
#### 내장영역 함수 확인
print(dir(__builtins__))


#### 지역변수, 전역변수
g=1
def testScope(a):
    global g  # global 키워드 사용
    g = 2  # 전역변수 값 변경
    return g + a
print(testScope(1))
print(g)


#### 키워드 매개변수
def connectURI(server, port):
    return "http://" + server + ":" + port
print(connectURI(server='test.com', port='8080'))


#### 가변 매개변수
def testArgs(*args):   # 매개변수 TUPLE로 받음
    res = []
    for item in args:
        for x in item:
            if not x in res:
                res.append(x)
    return res
print(testArgs('HAN', 'JANG', 'SPAM'))


#### 미정의 매개변수
def userURIBuilder(server, port, **user):  # 매개변수 Dictionary로 받음
    str = "http://" + server + ":" + port + "?"
    for key in user.keys():
        str += key + '=' + user[key] + '&'
    return str
print(userURIBuilder('test.com', '80', id='userid', passwd='1234', name='mike'))


#### Lambda 함수(간단한 함수에 유용)
g = lambda x,y : x*y
print(g(2,3))
print( (lambda x: x*x)(3) )


#### enumerate() 함수 : 인덱스와 값 함께 반환
for i, value in enumerate(['TEST1', 'TEST2']):
    print(i, value)


#### 재귀 & doc 속성
def factorial(n):
    '''
    <DOC PART..>
    Return the Factorial of n, an exact integer >= 0
    '''
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))
print(help(factorial))





