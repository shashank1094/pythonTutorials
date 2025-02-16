# https://leetcode.com/problems/single-number-ii/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Loner.
        loner = 0

        # Iterate over all bits
        for shift in range(32):
            bit_sum = 0

            # For this bit, iterate over all integers
            for num in nums:
                # Compute the bit of num, and add it to bit_sum
                bit_sum += (num >> shift) & 1
                print(num, ">>" ,shift, f"{num:032b}",  num >> shift)
            # print(shift, bit_sum)
            # Compute the bit of loner and place it
            loner_bit = bit_sum % 3
            loner = loner | (loner_bit << shift)

        # Do not mistaken sign bit for MSB.
        if loner >= (1 << 31):
            loner = loner - (1 << 32)

        return loner

if __name__ == '__main__':
    print(Solution().singleNumber(nums = [-10,21,-10,21,-10,21,99]))
    print((1 << 31))