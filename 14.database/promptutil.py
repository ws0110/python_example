# coding: utf-8

'''
  콘솔에서 DB 실행하는 프로그램
'''

import sqlite3
import sys
import re

if len(sys.argv) == 2:
    path = sys.argv[1]
else:
    path = ':memory:'

con = sqlite3.connect(path)
con.isolation_level = None  ## 트랜잭션 없이 자동 커밋 설정
cur = con.cursor()

def printIntro():
    '프로그램 소개 메시지'
    print('pysqlite의 command 프로그램입니다.')
    print('특수 명령어는 ".help;"를 입력하세요.')
    print('SQL 구문은 ";"으로 끝나야 합니다.')

def printHelp():
    '도움말'
    print('.dump\t\t데이터베이스의 내용을 덤프 합니다')

def sqlDump(con, file=None):
    '데이터베이스 DUMP'
    if file != None:
        f = open(file, 'w')
    else:
        f = sys.stdout

    for i in con.iterdump():
        f.write('{0}\n', i)

    if f != sys.stdout:
        f.close()


printIntro()


buffer = "" ## 쿼리 버퍼

while True:
    line = input('pysqlite>>')
    if buffer == '' and line == '':
        break

    buffer += line

    if sqlite3.complete_statement(buffer):  ## ';'로 구문이 끝나는지 체크
        buffer = buffer.strip() ## 양쪽 공백 제거

        if buffer[0] == '.':
            cmd = re.sub('[;]', ' ', buffer).split()
            print('>>>>>>>>>>> ', cmd)
            if cmd[0] == '.help':
                printHelp()
            elif cmd[0] == '.dump':
                if len(cmd) == 2:
                    sqlDump(con, cmd[1])
                else:
                    sqlDump(con)

        else:
            try:
                buffer = buffer.strip()
                cur.execute(buffer)
                if buffer.lstrip().upper().startswith('SELECT'):
                    print(cur.fetchall())

            except sqlite3.Error as e:
                print('Error: ', e.args[0])

            else:
                print('구문이 성공적으로 수행되었습니다')

        buffer = ''


con.close()
print('프로그램을 종료합니다.')





