# coding: utf-8

'''
  queue 모듈
'''

import queue

def getItemList(q):
    ret = []
    n = q.qsize()  # qsize()
    while n > 0:
        ret.append(q.get())  # get()
        n -= 1
    return ret

l = 'apple,banana,orange'

q = queue.Queue()  ## 일반 큐
for i in l.split(','):
    q.put(i)
print(getItemList(q))

stack = queue.LifoQueue()   ## Stack
for i in l.split(','):
    stack.put(i)
print(getItemList(stack))

pq = queue.PriorityQueue()  ## 우선순위 큐
pq.put((5, 'apple'))
pq.put((10, 'banana'))
pq.put((1, 'orange'))
print(getItemList(pq))


q = queue.Queue(2)  ## 큐 사이즈 지정
q.put('A')
q.put('B')
# q.put('C')  # 무한 대기 상태
#print('test')
#q.put_nowait('C')  ## queue.Full 에러 발생

q.get()
q.get()
# q.get() ## 무한대기
# q.get_nowait() ## queue.Empty 에러발생


q = queue.Queue(2)  ## 큐 사이즈 지정
q.put('A')
q.put('B')
q.put('C', True, 5)  # 5초 대기 후 에러발생
q.get(True, 5)  # 5초 대기

