# coding: utf-8

########## 1

class Persion:
    name = 'Default Name'

p1 = Persion()
p1.name = 'Jang'
p2 = Persion()
print(p1.name, ' / ', p2.name)

Persion.title = 'Default Title' # Class 멤버 변수 추가
print(p1.title, ' / ', p2.title) ## 인스턴스에서 접근가능

p1.age = 20 ## 인스턴스 자체 멤버변수 추가
# print(p1.age, ' / ', p2.age)  ## ERROR!!

p1.__class__.name = 'Change Class Name'
print(p1.name, ' / ', p2.name, ' / ', p1.__class__.name)
p3 = Persion()
print(p3.name, ' / ', isinstance(p3, Persion))  ## isinstance 내장 함수



############ 2: 생성자, 소멸자

class MyClass:
    ''' 생성자 소멸자 테스트'''
    def __init__(self, value):
        self.value = value
        print('Class is created!! Value = ', self.value)

    def __del__(self):
        print('Class is deleted!')

def callMyClass():
    d = MyClass(10)
callMyClass()

############# 3: 정적메소드, 클래스 메소드

class CounterManager:
    ''' 생성된 인스턴스 객체 갯수 관리 '''
    __insCount = 0  ## 클래스 변수

    def __init__(self):
        CounterManager.__insCount += 1

    def staticPrintCount():  ## 정적 메소드(self 없음)
        print('Instance Count: ', CounterManager.__insCount)
    SPrintCount = staticmethod(staticPrintCount)  ## 정적 메소드 등록

    def classPrintCount(cls):  ## 클래스 메소드
        print('Instance Count: ', CounterManager.__insCount)
    CPrintCount = classmethod(classPrintCount)  ## 클래스 메소드 등록

a, b, c = CounterManager(), CounterManager(), CounterManager()
CounterManager.staticPrintCount()
a.classPrintCount()
CounterManager.SPrintCount()
a.SPrintCount()  ## 인스턴스로 정적 메소드 호출 가능(정적메소드 등록 하면)


############## 4: 연산자 중복 정의(+,-,*,/,//,%,pow(), <<, >>, &, |, abs(), ^, <,>,==,!= 등)

class GString:
    def __init__(self, init=None):
        self.content = init

    def __sub__(self, str):  ## - 연산자 재정의
        for i in str:
            self.content = self.content.replace(i, '')
        return  GString(self.content)

    def __abs__(self):  ## abs 연산자 재정의
        return GString(self.content.upper())

    def Print(self):
        print(self.content)

g1 = GString('aBcdef')
g1 = g1 - 'df'
g1.Print()
g1 = abs(g1)
g1.Print()


############## 4-1: 연산자 중복 정의(+,-,*,/,//,%,pow(), <<, >>, &, |, abs(), ^, <,>,==,!= 등)
class Sequencer:
    ''' 초기값을 받은 후 그 범위안에서 인덱스로 전달받은 값의 10배를 반환하는 클래스'''
    def __init__(self, maxValue):
        self.maxValue = maxValue

    def __len__(self):  ## len() 연산자 재정의
        return self.maxValue

    def __getitem__(self, index): ## A[i] 형식의 인덱스 참조 재정의
        if(0< index <= self.maxValue):
            return index * 10
        else:
            raise IndexError('Index out of range')

    def __contains__(self, item): ## in 재정의
        return (0 < item <= self.maxValue)

s = Sequencer(5)
print(s[1], ', ', s[3])
print(len(s))
print(3 in s)
print(10 in s)




############## 5: 상속
class Person:
    '부모 클래스'
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def printInfo(self):
        print('Info: Name:{0}, Phone:{1}'.format(self.name, self.phone))

    def printPersonData(self):
        print('Person: Name:{0}, Phone:{1}'.format(self.name, self.phone))

class Student(Person):
    '자식 클래스'
    def __init__(self, name, phone, subject, studentId):
        super().__init__(name, phone)  ## 부모 생성자 명시적 호출  "Person.__init__(self, name, phone) 로도 호출 가능"
        self.subject = subject
        self.studentId = studentId

    def printStudentData(self):
        print('Student: Subject:{0}, ID:{1}'.format(self.subject, self.studentId))

    def printInfo(self):  ### 메소드 재정의(매개변수, 리턴값 상관없이 메소드 이름만 같으면 재정의 됨)
        super().printInfo()  ## "Person.printInfo(self)" 로도 호출 가능
        print('Info: Subject:{0}, ID:{1}'.format(self.subject, self.studentId))

print(issubclass(Student, Person))
p = Person('Derick', '010-1234-5678')
print(p.__dict__)  ## 클래스 정보는 _"_dict__" 객체로 관리 됨
s = Student('Jang', '010-9876-1234', 'Title', '99099')
print(s.__dict__)
s.printPersonData()
s.printStudentData()
s.printInfo()


############## 5-1: 다중 상속
class Animal:
    def __init__(self):
        print('Animal INIT##')
    def cry(self):
        print('Animal Default Cry~~')

class Tiger(Animal):
    def __init__(self):
        super().__init__()
        print('Tiger INIT##')
    def cry(self):
        print('Tiger Cry~~')

    def jump(self):
        print('Tiger Jump!!')

class Lion(Animal):
    def __init__(self):
        super().__init__()
        print('Lion INIT##')
    def cry(self):
        print('Lion Cry~~')

    def bite(self):
        print('Lion Bite!!')

class Liger(Tiger, Lion):   ### 상속 선언 순서대로 메소드 참조 됨
    def __init__(self):
        super().__init__()
        print('Liger INIT##')
    def play(self):
        print('Liger Play..')

l = Liger()
l.jump()
l.bite()
l.cry()  ### ### 상속 선언 순서대로 메소드 참조 됨