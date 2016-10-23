
/*
    ctypes 테스트용 C 소스
    1. 컴파일 : gcc -c -fPIC ./ctypes_source.c
    2. shared library로 만들기
        : gcc -shared ctypes_source.o -o ctypes_source.so
        = 파이썬에서 'ctypes_source.so' 사용

*/

#include <stdio.h>

int multiply(int num1, int num2){
    return  num1 * num2;
}

