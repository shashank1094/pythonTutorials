# 560. Subarray Sum Equals K
from collections import defaultdict


class Solution(object):
    def subarray_sum_brute(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        for start_index in range(n):
            for end_index in range(start_index, n):
                sub_array = nums[start_index:end_index+1]
                if sum(sub_array) == k:
                    count+=1
                    print(sub_array)
        return count

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # Initialize with prefix sum 0 and count 1

        for num in nums:
            prefix_sum += num  # Update the running prefix sum
            if (prefix_sum - k) in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]  # Increment count if (prefix_sum - k) is found
            prefix_sum_count[prefix_sum] += 1  # Update the frequency of the current prefix sum

        return count

if __name__ == '__main__':
    print(Solution().subarray_sum_brute([3, 4, 7, 2, -3, 1, 4, 2, 1], 7))
    print(Solution().subarraySum([3,4,7,2,-3,1,4,2, 1], 7))
    print(Solution().subarray_sum_brute([3, 4, -7, 2, -3, 5, 1], 5))
    print(Solution().subarraySum([3, 4, -7, 2, -3, 5, 1], 5))