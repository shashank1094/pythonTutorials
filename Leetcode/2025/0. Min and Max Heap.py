# Python3 program to demonstrate heapq (Min Heap)
import heapq

# Create an empty heap
h = []
heapq.heapify(h)
# Add elements (multiplying by -1 to simulate Max Heap)
heapq.heappush(h, 20)
heapq.heappush(h, 30)
heapq.heappush(h, -10)
heapq.heappush(h, 400)
# Print min element
print("Min:", h[0])
# Print heap elements
print("Heap:", [i for i in h])
# Pop min element
heapq.heappop(h)
# Print heap after removal
print("Heap after pop:", [i for i in h])

def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)

# Python3 program to demonstrate heapq (Max Heap)
# Create an empty heap
h = []
heapq._heapify_max(h)
# Add elements (multiplying by -1 to simulate Max Heap)
_heappush_max(h, 10)
_heappush_max(h, 30)
_heappush_max(h, -20)
_heappush_max(h, 400)
# Print max element
print("Max:", h[0])
# Print heap elements
print("Heap:", [i for i in h])
# Pop max element
heapq._heappop_max(h)
# Print heap after removal
print("Heap after pop:", [i for i in h])

