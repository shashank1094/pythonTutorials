# https://leetcode.com/problems/house-robber/
from typing import List

# Time limit exceeded -
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#
#         def rob_from(_index):
#             if _index >= len(nums):
#                 return 0
#             return max(rob_from(_index+1), rob_from(_index+2) +nums[_index] )
#
#         return rob_from(0)

class Solution:
    def rob(self, nums: List[int]) -> int:
        memory = {}
        def rob_from(_index):
            if _index >= len(nums):
                return 0
            if _index in memory:
                return memory[_index]
            max_robbery_amount = max(rob_from(_index+1), rob_from(_index+2) +nums[_index] )
            memory[_index] = max_robbery_amount
            return max_robbery_amount
        return rob_from(0)


if __name__ == "__main__":
    print(Solution().rob([2,7,9,3,1]))