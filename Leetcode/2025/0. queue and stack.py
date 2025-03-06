from collections import deque

dq = deque([10, 20, 30])
dq.append(40)
dq.appendleft(5)
# extend(iterable)
dq.extend([50, 60, 70])
# extendleft(iterable)
dq.extendleft([0, 5])
# remove method
dq.remove(20)
# Remove elements from the right
print(dq.pop())
# Remove elements from the left
print(dq.popleft())




# Using its as stack
stack = deque()
stack.append('a')
stack.append('b')
print(stack.pop())
print(stack.pop())