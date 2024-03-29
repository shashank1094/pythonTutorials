# You are given an array of N integers, A1, A2 ,…, AN and an integer K.
# Return the of count of distinct numbers in all windows of size K.
#
# Formally, return an array of size N-K+1 where i’th element in this array contains number of
# distinct elements in sequence Ai, Ai+1 ,…, Ai+k-1.
#
# Note:
#
# If K > N, return empty array.
# For example,
#
# A=[1, 2, 1, 3, 4, 3] and K = 3
#
# All windows of size K are
#
# [1, 2, 1]
# [2, 1, 3]
# [1, 3, 4]
# [3, 4, 3]
#
# So, we return an array [2, 3, 3, 2].
from typing import List


class Solution:
    # @param A : list of integers
    # @param k : integer
    # @return a list of integers
    def dNums(self, A: List[int], k: int) -> List[int]:
        if k > len(A):
            return []
        else:
            return A


if __name__ == '__main__':
    sol2 = Solution()
    print(sol2.dNums([1, 2, 1, 3, 4, 3], 3))
