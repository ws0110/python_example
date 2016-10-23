# coding: utf-8

'''
 datetime 모듈 테스트
  - date 클래스
  - time 클래스
  - datetime 클래스
  - timedelta 클래스
'''

import datetime
import time

########## date 클래스 ##############

print(datetime.date(2016, 9,28))
print(datetime.date.fromtimestamp(time.time())) ## 타임스탬프 -> date 객체
print(datetime.date.today())  ## 오늘

d = datetime.date.today()
print(d.year, d.month, d.day, d.max, d.min)

d1 = d.replace(day=30)
print(d1)
print(d1.timetuple()) ## struct_time시퀀스 객체 변환
print(d1.weekday()) ## 월요일0, 일요일6

d2 = datetime.date.today()
print(d2)
print(d2.isoformat()) ## YYYY-MM-DD 형식 반환
print(d2.ctime())
print(d2.strftime('%y %m %d'))


########## time 클래스 ##############
print(datetime.time(hour=10, second=58))
print(datetime.time(8, 14, 20, 3000))

t = datetime.time(8, 14, 20, 3000)
print(t.replace(hour=17))
print(t.isoformat())
print(t.strftime('%H/%M/%S'))


########## datetime 클래스 ##############
dt = datetime.datetime(2016, 9, 29, hour=23, microsecond=31, second=50)
print(dt)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
print(dt.date())
print(dt.time())
print(dt.replace(year=1999))
print(dt.timetuple()) ## struct_time시퀀스 객체 변환
print(dt.weekday())
print(dt.isoformat())

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
print(datetime.datetime.fromtimestamp(time.time()))
print(datetime.datetime.utcfromtimestamp(time.time()))
dt2 = datetime.datetime.combine(datetime.date(2016,9,30), datetime.time(17))
print(dt2)


########## timedelta 클래스 ##############
print(datetime.timedelta(days=-3))  ## 3일 전
print(datetime.timedelta(hours=7))  ## 7시간 이후
print(datetime.timedelta(weeks=2, days=-3, hours=7)) ## 2주후 3일전 = 11일 후

td1 = datetime.timedelta(hours=7)
td2 = datetime.timedelta(days=-3)
print(td1 + td2)
print(td1 - td2)
print(td1 * 4)
print(td2 // 3)
print(td1 == td2)

d = datetime.date.today()
td = datetime.timedelta(days=3)
print(d + td)
print(d - td)

d2 = d.replace(day=20)
print(d - d2)

dt = datetime.datetime.today()
td = datetime.timedelta(hours=8)
print(dt + td)

