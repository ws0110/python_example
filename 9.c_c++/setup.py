# coding: utf-8

# 'python3 setup.py install' 빌드, 설치 동시에 실행
# 'python3 setup.py --help' 옵셥, 사용볍 확인 가능

from distutils.core import setup, Extension

spam_mod = Extension('spam', sources=['spammodule.c'])
setup(name="spam",
      version="1.0",
      description="A sample extension module",
      ext_modules = [spam_mod],
)