# coding: utf-8

def divide(a, b):
    return a/b

try:
    c = divide(5, 'a')
except (ZeroDivisionError, OverflowError, FloatingPointError):
    print('수식 관련 에러!')
except TypeError:
    print('타입 에러!!')
except Exception as e:
    print('에러!: ', e.args[0])
else:  # 예외 발생 안한 경우 실행
    print('Result: ', c)
finally:
    print('finished!!')


######### Exception 발생 : raise

def RaiseErrorFunc():
    raise NameError('Namer Error 전달 값')

def PropagateError():
    try:
        RaiseErrorFunc()
    except:
        print('에러 발생1')
        #raise  # 에러 상위로 전달

PropagateError()


########## 사용자 정의 Exception

class NegativeDivisionError(Exception):
    def __init__(self, value):
        self.value = value

def PositiviDivide(a, b):
    if(b < 0):
        raise NegativeDivisionError(b)
    return a/b

try:
    ret = PositiviDivide(10, -3)
except NegativeDivisionError as e:
    print('NegativeDivisionError!!: ', e.value)
except ZeroDivisionError as e:
    print('ZeroDivisionError!!: ', e.args[0])
except Exception as e:
    print(e.args)



############ assert

def foo(x):
    assert type(x) == int, 'Input Value must be Integer'
    return x * 10

print(foo('2'))
