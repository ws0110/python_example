# coding: utf-8

'''
  unittest 모듈
  pydoc
   - pydoc -p 7464 : 도움말 웹 브라우저 띄우기
'''

####### Simple ######

import unittest

def sum(a, b):
    return a+b

## Class1
class Module1Test(unittest.TestCase):  ## TestCase 상속
    def testSum1(self):  # 함수명은 test로 시작
        self.assertEqual(sum(1,2),3)


## Class2
class Module2Test(unittest.TestCase):
    def setUp(self):  ## SetUP 함수
        self.bags = [True, False]

    def tearDown(self):  ## 종료 함수
        del self.bags

    def testTrue(self):
        for item in self.bags:
            self.assertTrue(item)

### TestSuite(TestCase, TestSuite의 집합) 생성 ####
def makeSuite(testCase, tests):
    print(">>> ", map(testCase, tests))
    return unittest.TestSuite(map(testCase, tests))

if __name__ == '__main__':
    ## unittest.main()
    suite1 = makeSuite(Module1Test, ['testSum1'])
    #suite2 = makeSuite(Module2Test, ['testTrue'])

    allSuite = unittest.TestSuite([suite1])  ## suite2 뻈는데도 계속 테스트 실행됨??
    unittest.TextTestRunner(verbosity=2).run(allSuite)