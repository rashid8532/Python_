from collections import deque

d = deque([10,20,30])
print(d)
d.append(40)
print(d)
d.appendleft(5)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
