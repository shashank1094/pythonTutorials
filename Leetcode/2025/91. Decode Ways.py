# https://leetcode.com/problems/decode-ways/description/
from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        num_ways_decode = 0

        def helper(sub_str):
            nonlocal num_ways_decode
            if not len(sub_str):
                num_ways_decode += 1
                return
            if sub_str[0] == '0':
                return
            helper(sub_str[1:])
            two_digit = sub_str[:2]
            if 0 < int(two_digit) < 27:
                helper(sub_str[2:])
        helper(s)
        return num_ways_decode

class SolutionDP:
    @lru_cache(maxsize=None)
    def recursiveWithMemo(self, index, s) -> int:
        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1
        # If the string starts with a zero, it can't be decoded
        if s[index] == "0":
            return 0
        if index == len(s) - 1:
            return 1
        answer = self.recursiveWithMemo(index + 1, s)
        if int(s[index : index + 2]) <= 26:
            answer += self.recursiveWithMemo(index + 2, s)
        return answer

    def numDecodings(self, s: str) -> int:
        return self.recursiveWithMemo(0, s)

if __name__ == '__main__':
    print(SolutionDP().numDecodings("1111111111111111111111111111111111111111111111111111111111111"))
    print(Solution().numDecodings("111111111111111111111111111111"))