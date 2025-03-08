# https://leetcode.com/problems/trapping-rain-water/description/
from typing import List
import random

class Solution:
    # O(n) time and O(n) space
    def trap_unoptimised(self, heights: List[int]) -> int:
        n = len(heights)
        max_left_prefix = [0] * n
        max_right_prefix = [0] * n
        max_left = 0
        for i in range(n):
            max_left = max(max_left, heights[i])
            max_left_prefix[i] = max_left
        max_right = 0
        for i in range(n-1, -1,-1):
            max_right = max(max_right, heights[i])
            max_right_prefix[i] = max_right
        water_trapped = 0
        for i in range(n):
            water_trapped += min(max_left_prefix[i], max_right_prefix[i]) - heights[i]
        return water_trapped

    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        water_trapped = 0
        max_left = heights[0]
        max_right = heights[n-1]
        left_index = 0
        right_index = n-1
        while left_index < right_index:
            if heights[left_index] > heights[right_index]:
                max_right = max(max_right, heights[right_index])
                water_trapped+=(max_right - heights[right_index])
                right_index-=1
            else:
                max_left = max(max_left, heights[left_index])
                water_trapped += (max_left - heights[left_index])
                left_index+=1
        return water_trapped


if __name__ == '__main__':
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))