# https://leetcode.com/problems/longest-increasing-subsequence/


class Solution:
    def __init__(self):
        self.len_of_max_lis = 0
        self.dp = {0 : 0}

    def lengthOfLIS(self, nums) -> int:
        self.util(nums, len(nums))
        return self.len_of_max_lis

    def util(self, nums, n):
        if self.dp.get(n) is not None:
            return self.dp.get(n)
        if n == 1:
            self.len_of_max_lis = max(self.len_of_max_lis, 1)
            return 1
        max_till_now = 1
        for i in range(1, n):
            res = self.util(nums, i)
            if nums[n - 1] > nums[i - 1] and res + 1 > max_till_now:
                max_till_now = res + 1
        self.len_of_max_lis = max(self.len_of_max_lis, max_till_now)
        self.dp[n] = max_till_now
        return max_till_now


if __name__ == '__main__':
    print(Solution().lengthOfLIS([1]))


