# coding: utf-8

'''
  socket 모듈
    - socket CLIENT
'''

import socket

HOST = '127.0.0.1'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.send(b'Hello Socket!!')
data = s.recv(1024)
s.close()
print('Received: ', data)