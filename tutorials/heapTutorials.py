# https://docs.python.org/3.7/library/heapq.html
import heapq

list_ = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heap = []
for value in list_:
    heapq.heappush(heap, value)
    print('Pushed : {}, Heap : {}'.format(value, heap))

# Transform list x into a heap, in-place, in linear time using heapq.heapify(list_)
print('Final : ', heap)

for i in range(len(heap)):
    print('Popped : {}, Heap : {}'.format(heapq.heappop(heap), heap))

# MaxHeaps : https://www.interviewbit.com/problems/kth-smallest-element-in-the-array/

# A = [ 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16,
#  66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 ]
# k = 9
#
# k_min_elems = A[:k]
# k_min_elems = list(k_min_elems)
# import heapq
#
# heapq._heapify_max(k_min_elems)
# for elem in A[k:]:
#     if k_min_elems[0] >= elem:
#         heapq._heapreplace_max(k_min_elems, elem)
#
# print(k_min_elems[0])
