# coding: utf-8

'''
  smtplib 모듈
    - TEXT 메일 테스트
'''

import smtplib
from email.mime.text import MIMEText

SMTP_HOST = 'smtp.gmail.com:587'
TEXT = '한글 테스트'
SENDER_ADDR = 'ws010110@gmail.com'
RECIVE_ADDR = 'ws010110@gmail.com'

msg = MIMEText(TEXT)
msg['Subject'] = '테스트 제목'
msg['From'] = SENDER_ADDR
msg['TO'] = RECIVE_ADDR

s = smtplib.SMTP(SMTP_HOST)
s.ehlo()
s.starttls()
s.ehlo()
s.login(SENDER_ADDR, 'ws471567')
s.ehlo()
print(msg.as_string())
s.sendmail(SENDER_ADDR, [RECIVE_ADDR], msg.as_string())
s.close()

