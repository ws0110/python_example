# coding: utf-8

'''
  os.path 모듈
  glob
'''

print('------------------ os.path -------------------')
import time
import os

print(os.path.abspath('test'))  ## 입력받은 경로 -> 절대경로로 변경
print(os.path.basename('/Users/ws0110/Study/Develop/Python/mytest3/13.filesystem/test'))  ## 젇대경로 -> 상대경로
print(os.path.dirname('/Users/ws0110/Study/Develop/Python/mytest3/13.filesystem/ex_filesystem.py'))  ## 디렉토리명만 리턴
print(os.path.exists('/Users/ws0110/Study/Develop/Python/mytest3/13.filesystem')) ## 읽기권한 없어도 False 반환가능
print(os.path.expanduser('~/test'))  ## 사용자 경로 절대경로로 변환
print(os.path.expandvars('$HOME')) ## 환경변수 정의 변환
print(os.environ)  ## 환경변수
print(time.localtime(os.path.getatime('/Users/ws0110/Study/Develop/Python/mytest3/13.filesystem/ex_filesystem.py')))  ## 파일,폴더 최근 접근시간 리턴
print(time.localtime(os.path.getmtime('/Users/ws0110/Study/Develop/Python/mytest3/13.filesystem/ex_filesystem.py')))  ## 파일,폴더 최근 변경시간 리턴
print(time.localtime(os.path.getctime('/Users/ws0110/Study/Develop/Python/mytest3/13.filesystem/ex_filesystem.py')))  ## 파일,폴더 생성시간 리턴
print(os.path.getsize('/Users/ws0110/Study/Develop/Python/mytest3/13.filesystem/ex_filesystem.py')) ## 사이즈 리턴(Byte)
print(os.path.isfile('/Users/ws0110/Study/Develop/Python/mytest3/13.filesystem')) ## 파일인지 판단
print(os.path.isdir('/Users/ws0110/Study/Develop/Python/mytest3/13.filesystem')) ## 디렉토리 인지 판단
print(os.path.join('/Users', 'ws0110', 'test'))  # 입력받은 경로 연결
print(os.path.split('/Users/ws0110/Study/Develop/Python/mytest3/13.filesystem/ex_filesystem.py'))  ## 파일, 디렉토리 분리(파일검사 없음, 문자열장난)


################## glob (ls와 비슷한 기능) ######################
import glob
print('------------------ glob -------------------')
print(glob.glob('*.py'))
print(glob.glob('../*'))
print(glob.iglob('*'))  ## iterator 객체로 반환

