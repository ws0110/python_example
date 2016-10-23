
'''
 배포를 위한 SetUP 파일
    - 패키지 제작 시 필요한 코드들은 setup.py가 있는 곳에 같이 위치해야 함
    - 실행: python3 setup.py sdist : Source 배포
           python3 setup.py bdist : Binary로 배포

    - 설치 : 압축풀고 -> python3 setup.py install 실행

'''

from distutils.core import setup

setup(name='book',
      version='1.0',
      py_modules=['bookmgmt'],

      ## Package 단위 배포
      # classifiers= ['animal', 'animal::birl::penguin', 'animal::bird::sparrow', 'animal.mammal.human'],  # 모듈
      # packages=['animal', 'annimal.bird', 'animal.mammal'] # 패키지
      )