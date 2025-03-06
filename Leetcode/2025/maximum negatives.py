import heapq
import random

class Solution:
    def getMaxNegativePnL(self, arr: list[int]) -> int:
        def _heappush_max(heap, item):
            heap.append(item)
            heapq._siftdown_max(heap, 0, len(heap) - 1)

        negatives_till_now = []
        heapq._heapify_max(negatives_till_now)
        sum_till_now = 0

        for current_number in arr:
            if sum_till_now - current_number < 0:
                if len(negatives_till_now) == 0:
                    sum_till_now += current_number
                else:
                    peek = negatives_till_now[0]
                    if current_number < peek:
                        sum_till_now += peek * 2
                        sum_till_now -= current_number
                        heapq._heappop_max(negatives_till_now)
                        _heappush_max(negatives_till_now, current_number)
                    else:
                        sum_till_now += current_number
            else:
                _heappush_max(negatives_till_now, current_number)
                sum_till_now -= current_number
        return len(negatives_till_now)

if __name__ == '__main__':
    print(Solution().getMaxNegativePnL(random.sample(range(1, 10), 6)))
    print(Solution().getMaxNegativePnL([7, 9, 6, 1, 8, 3]))
    print(Solution().getMaxNegativePnL([1,1,1,1]))
# [7, 9, 6, 1, 8, 3]
# [7 16 22 23 31 34] prefix
# [34 27 18 12 11 3] suffix
 