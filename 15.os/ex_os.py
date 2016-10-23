# coding: utf-8

'''
  os 모듈
'''

import os

print(os.name)
print(os.getpid())
print(os.environ.keys())
print(os.environ['HOME'])
print(os.getenv('homepath', 'FUCK!!'))
os.putenv('TEST_ENV', 'TEST Value')  ## 환경변수 등록 : 자식 프로세스에 영향을 줌

print(os.getcwd())
os.chdir('tmp')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())


print(os.access('.', os.F_OK)) ## F_OK: 존재여부
print(os.access('.', os.R_OK)) ## R_OK: 읽기 가능
print(os.access('.', os.W_OK)) ## W_OK: 쓰기 가능
print(os.access('.', os.X_OK)) ## X_OK: 샐행 가능

print(os.listdir('..'))

#os.makedirs('child1/child2')
#os.rename('child1/child2', 'child1/rename')
#os.renames('child1/child2', 'child1/rename/child2')  # 디렉토리 생성
#os.removedirs('child1/rename')

print(os.stat('.'))

for path, dirs, files in os.walk('..'):
    print(path, dirs, files)

print(os.pipe())  ## 읽기, 쓰기 전용 파이프 파일 디스크립터 반환(프로세스간 통신 시 사용)
r, w = os.pipe()
rd = os.fdopen(r)  ## 파일 디스크립터를 이용해 파일객체 생성


p = os.popen('ls -al', 'r')  ## 명령 실행
print(p.read())

os.system('ls -al') ## 성공 시 0 리턴

print(os.strerror(1)) # 코드에 해당하는 에러 메시지 출력


