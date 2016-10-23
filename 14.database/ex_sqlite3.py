# coding: utf-8

'''
  sqlite3 모듈
'''

import sqlite3

#con = sqlite3.connect('test.db')
con = sqlite3.connect(':memory:')  # 메모리 DB
cursor = con.cursor()
cursor.execute('CREATE TABLE PhoneBook(Name text, PhoneNumber text)')
cursor.execute('INSERT INTO PhoneBook VALUES(?, ?)', ('name', '010-1111-2222'))
datalist = (('Tome', '011-1111-2345'), ('DSP', '012-4444-5555'))
cursor.executemany('INSERT INTO PhoneBook VALUES(?, ?)', datalist)

cursor.execute('SELECT * FROM PhoneBook')
for row in cursor:
    print('row> ', row)

cursor.execute('SELECT * FROM PhoneBook')
print(cursor.fetchone())

cursor.execute('SELECT * FROM PhoneBook')
print(cursor.fetchmany(2))

cursor.execute('SELECT * FROM PhoneBook ORDER BY Name')
print(cursor.fetchall())

### 사용자 정의 정렬 ###
# 2개 매개변수를 받고, str1<str2 음수리턴, 같으면 0, str1>str2 양수리턴 규칙에 맞게 작성
def OrderFunc(str1, str2):
    s1 = str1.upper()
    s2 = str2.upper()
    return (s1 > s2) - (s1 < s2)
con.create_collation('myorder', OrderFunc)  ## 함수 등록
cursor.execute('SELECT * FROM PhoneBook ORDER BY Name COLLATE myorder ')
print(cursor.fetchall())


############## 내장 함수 사용 ################

cursor.execute('CREATE TABLE AgeBook(Name text, Age integer);')
datalist2 = (('Tome', 20), ('DSP', 30))
cursor.executemany('INSERT INTO AgeBook VALUES(?, ?);', datalist2)
cursor.execute('SELECT min(Age), max(Age), sum(Age), length(Name), count(*) FROM AgeBook ;')
print(cursor.fetchall())

### 사용자 정의 집계 함수 작성 ###
class Average:
    def __init__(self):
        self.sum = 0
        self.cnt = 0

    def step(self, value):
        ''' 인자를 받는 함수(반드시 필요) '''
        self.sum += value
        self.cnt += 1

    def finalize(self):
        ''' 결과 리턴하는 함수(반드시 필요) '''
        return self.sum/self.cnt

con.create_aggregate('avg', 1, Average)  ## 함수 등록(이름 인자갯수, 클래스명)
cursor.execute('SELECT avg(Age) FROM AgeBook ;')
print(cursor.fetchall())


############## 사용자 정의 자료형 ################

## 사용자 정의 클래스
class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "Point(%f, %f)" % (self.x, self.y)


## Adapter(클래스 -> DB 이용가능 객체로)
def PointAdapter(point):
    return '%f:%f' % (point.x, point.y)


## Convertor(DB 자료 -> 클래스 형태로)
def PointConverter(str):
    x, y = list(map(float, str.decode().split(':')))
    return Point(x, y)

sqlite3.register_adapter(Point, PointAdapter)  ## Adapter 등록
sqlite3.register_converter('point', PointConverter) ## Convertoer 등록

p = Point(4, -3.2)
cursor.execute('CREATE TABLE Test(Pnt point);')
cursor.execute('INSERT INTO Test VALUES(?);', (p, ))
cursor.execute('SELECT Pnt FROM Test ;')
print(cursor.fetchall())




############## DataBase 덤프 ################
with open('dump.sql', 'w') as f:
    for i in con.iterdump():
        f.write('{0}\n'.format(i))





cursor.close()
con.close()