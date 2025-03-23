# https://leetcode.com/problems/next-greater-element-i/
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len_n1 = len(nums1)
        ans = [-1] * len_n1
        memo = {}
        for i2, n2 in enumerate(nums2):
            for remaining_num in nums2[i2+1:]:
                if remaining_num > n2:
                    memo[n2] = remaining_num
                    break
        for i1, n1 in enumerate(nums1):
            max_after_n = memo.get(n1, -1)
            ans[i1] = max_after_n
        return ans


if __name__ == '__main__':
    print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))
