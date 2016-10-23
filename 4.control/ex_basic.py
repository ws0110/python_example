# coding: utf-8

### 조건 비교 방법
score = int(input('Input Score: '))
if 90<= score <= 100:
    grade = 'A'
elif 80<= score < 90:
    grade = 'B'
else:
    grade = 'C'

print('grade: ', grade)


##### True, False 판단
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool())
print(bool(''))
print(bool({}))
print(bool(None))

##### print Format
print('--{0}, {1}, {2}--'.format(100, 99, 80))

#### for, while에서 break로 중간에 종료 되지 않으면 else 블럭 실행
L = [1, 2, 13, 4, 5]
for i in L:
    if i == 3:
        break
else:
    print('Not Break!!')