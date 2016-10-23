

#### String
str = 'python'
print(str[0:1])
print(str[:2])
print(str[2:])
print(str[-2:])
print(str[:])
print(str[2::])
print(str[::2])
print('----------------------------')

#### List
colors = ['red', 'green', 'gold']
colors.append('blue')
print(colors)
colors.insert(0, 'black')
print(colors)
colors.extend(['white', 'gray'])
print(colors)
print(colors.count('red'))
print(colors.pop())
print(colors.pop(0))
print(colors)
colors.remove('blue')
print(colors)
colors.sort()  # 정렬
print(colors)
colors.reverse()  # 정렬
print(colors)
print('red' in colors)

def mysort(x):
    return x[-1]   # Custom 정렬(ex.마지막 단어 기준)
colors.sort(key=mysort)
print(colors)

print('----------------------------')

#### SET
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(type(set1))
print(set1 | set2)  # 합집합
print(set1 & set2) # 교집합
print(set1 - set2) # 차집합
print(3 in set1)
print('----------------------------')

#### TUPLE : ()로 사용 읽기전용(LIST보다 빠름)
tp1 = (1, 2, 3)
print(type(tp1))
(tp2, tp3) = (1, 3), (2, 4)
print(tp2)
print(3 in tp1)
print('----------------------------')

#### Type 변환
list1 = list(tp1)
print(list1) # typle -> list
set9 = set(list1)
print(set9)
tuple1 = tuple(set9)
print(tuple1)
print('----------------------------')

#### Dictionary
d = dict(a=1, b=2, c=3)
print(d)
d2 = {'apple':'red', 'banana':'yellow'}
print(d2)
print(d2['apple'])
d2['cherry'] = 'red'
print(d2)
for k, v in d2.items():
    print(k, v)
for k in d2.keys():
    print(k)
for v in d2.values():
    print(v)
del d2['cherry']
print(d2)
d2.clear()
print(d2)
print('----------------------------')

####### COPY
a = [1, 2, 3]
b = a
a[0] = 38
print(a, ' : ', b)
c = a[:]
a[0] = 1
print(a, ' : ', c)






