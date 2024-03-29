# The set [1,2,3,…,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3 ) :
#
# 1. "123"
# 2. "132"
# 3. "213"
# 4. "231"
# 5. "312"
# 6. "321"
# Given n and k, return the kth permutation sequence.
#
# For example, given n = 3, k = 4, ans = "231"
#
#  Good questions to ask the interviewer :
# What if n is greater than 10. How should multiple digit numbers be represented in string?
#  In this case, just concatenate the number to the answer.
# so if n = 11, k = 1, ans = "1234567891011"
# Whats the maximum value of n and k?
#  In this case, k will be a positive integer thats less than INT_MAX.
#  n is reasonable enough to make sure the answer does not bloat up a lot.
#  NOTE: You only need to implement the given function. Do not read input,
#        instead use the arguments to the function. Do not print the output,
#        instead return values as specified. Still have a doubt? Checkout Sample Codes for more details.
import math


class Solution:

    @staticmethod
    def getPermutation(n, k):
        def helper(options, tmp_k):
            if not options:
                return
            nonlocal result
            options_left = math.factorial(len(options) - 1)
            index = math.ceil(tmp_k / options_left)
            index -= 1
            result += str(options.pop(index))
            helper(options, tmp_k % options_left)

        result = ''
        helper([i for i in range(1, n + 1)], k)
        return result


if __name__ == '__main__':
    sol1 = Solution()
    print(sol1.getPermutation(8, 18))

