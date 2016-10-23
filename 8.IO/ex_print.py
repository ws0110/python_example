# coding: utf-8

import sys

print('a','b' + 'c')

print('A', 'B', sep='-', end='!!', file=sys.stderr)

##### String 정렬
print('ABC'.rjust(5))
print('ABC'.ljust(5), 'D')
print('ABC'.center(5))
print('ABC'.zfill(5))


##### format
print('{0}, {1}'.format('a', 'b'))
print('{A}, {B}'.format(A='a', B='b'))
dic = {'A': 'a', 'B':'b'}
print('{0[A]}, {0[B]}'.format(dic))
print('{A}, {B}'.format(**dic))
numbers = [5, 4, 3, 2, 1]
print('{numbers}'.format(**locals()))  ## vars(), locals()
print('{0:.3f}'.format(4/3))

## format 정렬 (>, <, ^, =)
print('{0:$>5}'.format(10))
print('{0:$<5}'.format(10))
print('{0:$^5}'.format(10))