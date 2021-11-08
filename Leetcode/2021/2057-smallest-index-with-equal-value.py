from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        import sys
        _min = sys.maxsize
        for indx in range(len(nums)):
            if (indx % 10) == (nums[indx]):
                if _min > indx:
                    _min = indx
        return -1 if _min == sys.maxsize else _min


if __name__ == '__main__':
    a = Solution().smallestEqual(
        [6, 5, 4, 4, 9, 1, 5, 0, 8, 8, 5, 8, 0, 9, 8, 3, 6, 5, 2, 7, 7, 6, 6, 8, 9, 6, 5, 6, 5, 6, 8, 6, 9, 5, 1, 0, 5,
         5])
    print(a)