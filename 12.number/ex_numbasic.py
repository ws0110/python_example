# coding: utf-8

'''
 숫자 관련 기본
  - 내장 함수
  - math 모듈
  - fractions 모듈
  - decimal 모듈
  - random 모듈
'''

########## 내장 함수 ##############

l = list(range(0,10))
print(l)
print(sum(l))
print(max(l))
print(min(l))
print(abs(-11))
print(pow(2, 10))
print(divmod(7, 4))

print(round(123.4567))
print(round(123.4567, 2))
print(round(123.4567, -1))  ## -는 정수 자리에서 반올림


########## math ##############

import math

print(math.ceil(123.456)) # 올림
print(math.floor(123.956))  # 내림
print(math.trunc(123.456)) # 버림
print(math.copysign(100, -0.0)) # 부호 복사
print(math.fabs(-123)) # 절대값
print(math.factorial(5))
print(math.fsum([1,2,3]))
print(math.modf(-16.7))  # 소수, 정수 분리
print(math.fmod(5.5, 3), 5.5%3)
print(math.fmod(-5.5, 3), -5.5%3)  ## 결과 다름!!!(보통 정수는 %사용, 소수점은 fmod()사용 함# )

print(math.pow(2, 10))
print(math.sqrt(2))
print(math.log(4,2))
print(math.gcd(120, 180))  ## 최대공약수 구하기


########## fractions (유리수) ##############
import fractions
print(fractions.Fraction(4, 16)) ## 공약수가 존재하는 경우 자동으로 제거 됨
print(fractions.Fraction(-6, 21))
print(fractions.Fraction(4))
print(fractions.Fraction('4/16'))  ## 문자열로 생성
print(fractions.Fraction('3.14'))
print(fractions.Fraction('  -0.34   '))  ## 공백제거
print(fractions.Fraction.from_float(0.5))  ## float값으로 생성
print(fractions.Fraction.from_decimal(4))  ## 10진수로 생성

print(fractions.Fraction.from_float(math.pi))
print(fractions.Fraction.from_float(math.pi).limit_denominator(100))  ## 분모가 100보다 작은 객체로 생성

f = fractions.Fraction.from_float(3.14)
print(math.floor(f)) ## 내림
print(math.ceil(f)) ## 올림
print(round(f))  ## 반올림


########## Decimal (십진수) : 실수를 표현(float보다 정확함) ##############

import decimal
print(decimal.Decimal(3))
print(decimal.Decimal('1.1'))
print(decimal.Decimal(str(1/7)))
print(decimal.Decimal('-0'))
print(decimal.Decimal('NaN'))
print(decimal.Decimal((1, (3,1,4), -2)))  ## 튜플(부호, 지수, 가수)

a, b = decimal.Decimal('3.14'), decimal.Decimal('0.4')
print(a+b)
print(math.ceil(a))
print(sum([a, b]))

print(a.compare(b))  ## a>b:1, a<b:-1, a=b:0 리턴
print(a.is_finite())
print(a.is_zero())

#### Decimal 환경설정 ###
print(decimal.DefaultContext)
print(decimal.BasicContext)
print(decimal.ExtendedContext)
print(decimal.getcontext())  ## 현재 설정 조회

d1, d2 = decimal.Decimal(3.14), decimal.Decimal(7)
print(d1/d2)
decimal.getcontext().prec = 7  ## 환경설정 변경
print(d1/d2)
decimal.getcontext().rounding = decimal.ROUND_CEILING  ## 반올림 환경설정 변경
print(d1/d2)

decimal.setcontext(decimal.BasicContext)
print(d1/d2)



########## random 모듈 ##############
print('-------------------- random --------------------')
import random
print(random.random()) ## 0<= N <1 값 리턴
print(random.uniform(11, 20))  ## 입력받은 2값사이의 임의 float값 출력
for i in range(3):
    print(random.gauss(1, 1.0))  ## 평균1, 표준편차:0.1 인 정규분포 난수를 구함

print(list( random.randrange(20) for i in range(10) ))
print( random.sample(range(20), 10) )  ## 0~19 중 10개를 중복없이 랜덤으로 리턴
print(list( random.randrange(0,  20, 3) for i in range(10) ))  ## 3의 배수 출력(중복 가능)

l = list(range(10))
print(list( random.choice(l) for i in range(5) ))  ## 시퀀스 객체에서 임의의 값 5개 추출(중복 가능)
print( random.sample(l, 5) )  ## 중복없이 5개 추출

print(l)
random.shuffle(l)  ## 값 섞기(객체 자체를 변경함)
print(l)

l2 = list(range(10))
print(l2)
print( random.sample(l2, len(l2)) )  ## 값 섞기와 같은 효과(객체 자체 변경 안됨)
print(l2)







