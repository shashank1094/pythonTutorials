# https://docs.python.org/3.7/library/heapq.html
import heapq

list_ = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heap = []
for value in list_:
    heapq.heappush(heap, value)
    print(heap)

# Transform list x into a heap, in-place, in linear time using heapq.heapify(list_)
print('Final : ', heap)

print([heapq.heappop(heap) for i in range(len(heap))])
