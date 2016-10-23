# coding: utf-8

'''
  smtplib 모듈
    - Multipart 메일 테스트
'''

import smtplib
import mimetypes

from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

## Global
SMTP_HOST = 'smtp.gmail.com:587'
TEXT = '한글 테스트'
SENDER_ADDR = 'ws010110@gmail.com'
RECIVE_ADDR = 'ws010110@naver.com'
HTML_FILE = 'logo.html'
IMAGE_FILE = 'logo.gif'

msg = MIMEBase('multipart', 'mixed') ## Image, Text 등을 담기 위해 MIMEBase 생성
msg['Subject'] = '테스트 제목'
msg['From'] = SENDER_ADDR
msg['TO'] = RECIVE_ADDR

## html 생성(MIMEText)
htmlFD = open(HTML_FILE, 'rb')
htmlPart = MIMEText(htmlFD.read(),'html', _charset='utf-8')  ## subType을 html로 셋팅
htmlFD.close()

## Image 생성(MIMEImage)
imageFD = open(IMAGE_FILE, 'rb')
imagePart = MIMEImage(imageFD.read())
imageFD.close()

msg.attach(imagePart)
msg.attach(htmlPart)

msg.add_header('Content-Disposition', 'attachment', filename=IMAGE_FILE) ## 첨부파일 정보 추가

s = smtplib.SMTP(SMTP_HOST)
s.set_debuglevel(1)  ## 디버깅 레벨 설정
#print(s.ehlo())
s.starttls()
#print(s.ehlo())
s.login(SENDER_ADDR, 'ws471567')
#print(s.ehlo())
#print(msg.as_string())
s.sendmail(SENDER_ADDR, [RECIVE_ADDR], msg.as_string())
s.close()



