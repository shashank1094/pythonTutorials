from collections import deque

def increasing_monotonic_queue(arr, n):
	q = deque()
	for i in range(n):
		while len(q) > 0 and q[-1] > arr[i]:
			q.pop()
		q.append(arr[i])
	return q

arr = [3,4,1,5,2,6]
n = len(arr)
q = increasing_monotonic_queue(arr, n)
for i in q:
	print(i, end=' ')
