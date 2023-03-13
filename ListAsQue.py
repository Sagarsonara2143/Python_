'''   List as Que  ---  FIFO   '''

from _collections import deque


l = deque([])

l.append("Python")
print(list(l))
l.append(20)
print(list(l))
l.append('Java')
print(list(l))
l.append(30)
print(list(l))
l.append(True)
print(list(l))

l.popleft()
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))
