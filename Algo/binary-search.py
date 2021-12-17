# https://leetcode.com/problems/binary-search/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            curr = nums[mid]
            if curr == target:
                return mid
            if target < curr:
                end = mid - 1
                continue
            else:
                start = mid + 1
                continue
        return -1


if __name__ == '__main__':
    print(Solution().search([-1, 0, 3, 5, 9, 12], 2))
