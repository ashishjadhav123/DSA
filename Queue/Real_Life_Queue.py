
from collections import deque

queue = deque()

queue.append(5)
queue.append(10)
queue.append(15)
queue.append(20)

print(queue)

# Dqueue
print(queue.popleft())

# Peek

print(queue[0])