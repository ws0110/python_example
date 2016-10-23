# coding: utf-8

'''
  socket 모듈
    - socket SERVER
'''

import socket

HOST = '' # 호스트 지정안하면 가능한 모든 인터페이스 의미
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print('connected by ', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)
conn.close()


