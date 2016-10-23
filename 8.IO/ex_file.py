# coding: utf-8

f1 = open('test.txt', 'w')
cnt = f1.write('test file!!\n2 line')
f1.close()
print(cnt)
f1 = open('test.txt', 'r')
print(f1.read())
f1.close()

## 파일 복사
'''
f2 = open('copy.mp3', 'wb')
f2.write(open('EndlessRain.mp3', 'rb').read())
f2.close()
'''

## readline(), readlines(), seek(), tell()
f3 = open('test.txt', 'r')
print(f3.read())
print(f3.read())
print(f3.tell())
f3.seek(0)
print(f3.readline())
f3.seek(0)
print(f3.readlines())
f3.close()

## with
with open('test.txt', 'r') as f:  # close() 필요없음
    print(f.readlines())

##### Pickle (Class, List, Set, Dict 등 저장,로드)
import pickle
colors = ['red', 'green', 'blue']
with open('colors', 'wb') as f:
    pickle.dump(colors, f)

with open('colors', 'rb') as f:
    colors2 = pickle.load(f)
    print(colors2)


class test:
    var = None
a = test()
a.var = 'TEST'

with open('class', 'wb') as f:
    pickle.dump(a, f)

with open('class', 'rb') as f:
    a2 = pickle.load(f)
    print(a2.var)


