
// '모듈이름+module.c' 형식의 파일이름 주로 사용

#include <python.h>



// strlen 메소드 정의
static PyObject* spam_strlen(PyObject *self, PyObject *args)
{
    const char* str=NULL;
    int len=0;

    // format: i(int), s(const char*), f(float), l(long), y(const char*), u(Py_UNICODE)
    //         EX> PyArg_ParseTuple(args, "lls", &k, &l, &str)
    if(!PyArg_ParseTuple(args, "s", &str))   // PyArg_parseTuple(): 파이썬에서 전달된 인수를 C자료형으로 변환(str지역변수에 값 할당)
        return NULL;

    len = strlen(str);

    return Py_BuildValue("i", len); // C자료형값을 파이썬이 인식가능한 PyObject로 변경

};


// 나누기 메소드 정의
static PyObject* spam_division(PyObject *self, PyObject *args)
{
    int quotient=0;
    int dividend, divisor = 0;

    if(!PyArg_ParseTuple(args, "ii", &dividend, &divisor))
        return NULL;

    if(divisor){  // 0이 아니면
        quotient = dividend/divisor;

    } else{   // 사용자 정의 메소드는 예외 직접 처리 필요!!!!
        PyErr_SetString(PyExc_ZeroDivisionError, "divisor must not be 0[User Defined Excepton!!!]");
        return NULL;
    }

    return Py_BuildValue("i", quotient);
};



// 메소드 정의
static PyMethodDef SpamMethods[] = {
    {"strlen"   // 파이썬에서 사용하는 함수명
     , spam_strlen  // 실행되는 함수 포인터
     , METH_VARARGS // 매개변수 전달 방식(튜플형태로 전달)
     , "count a string length"
     },
     {"division", spam_division, METH_VARARGS, "division exception test method" },
     {NULL, NULL, 0, NULL}  // 배열의 끝을 표시
};

// 모듈 정의
static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",  // 모듈이름
    "It is test module",  // 모듈 설명(__doc__에 저장)
    -1,
    SpamMethods
};

// 초기화 메소드
PyMODINIT_FUNC
PyInit_spam(void)  // 'PyInit_모듈명' 형식
{
    return PyModule_Create(&spammodule);
}


