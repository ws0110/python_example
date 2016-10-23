# coding: utf-8

'''
 time 모듈
'''

import time

print(time.time()) ## 현재 타임스탬프
print(time.gmtime())  ## struct_time 시퀀스 객체 리턴( <- 타임스탬프)
print(time.localtime())  ## Local struct_time 시퀀스 객체 리턴( <- 타임스탬프)

t = time.gmtime(1234567890)
print(t)
print(t.tm_year)
print(time.asctime(t))
print(time.mktime(t))  # struct_time 시퀀스 객체 -> 타임스탬프 변환

t1 = time.time()
time.sleep(1) ## sleep() 메소드
t2 = time.time()
print('Sleep: ', (t2-t1))


#### 사용자 정의 포맷 strftime(), strptime() #######
print(time.strftime('%B %dth %A %I:%M %p', time.gmtime()))
print(time.strftime('%Y-%m-%d %H:%M:%S %a', time.localtime()))
print(time.strftime('%Y-%m-%d %H:%M:%S %a'))  ## 매개변수 없는 경우 현재 Localtime 표시

timestring = time.ctime()
print(time.strptime(timestring))

format = '%Y-%m-%d %H:%M:%S %a'
timestring = time.strftime(format)
print(time.strptime(timestring, format))