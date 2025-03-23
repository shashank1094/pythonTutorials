# https://leetcode.com/problems/longest-valid-parentheses/description/
from collections import deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def is_valid(_str):
            if not len(_str):
                return True
            stack = deque()
            for i in range(len(_str)):
                if _str[i] == '(':
                    stack.append(_str[i])
                else:
                    if len(stack):
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0

        n = len(s)
        max_len = 0
        for i in range(n):
            for j in range(i, n):
                sub_str = s[i:j+1]
                if is_valid(sub_str):
                    max_len = max(max_len, len(sub_str))
        return max_len


# Python Solution
# Not so obvious
class SolutionImproved:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len


class SolutionDP:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = (
                        dp[i - 1]
                        + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)
                        + 2
                    )
                maxans = max(maxans, dp[i])
        # print(dp)
        return maxans

if __name__ == '__main__':
    print(Solution().longestValidParentheses('())((()))'))
    print(SolutionImproved().longestValidParentheses('())((()))'))
    print(SolutionDP().longestValidParentheses('())((()))'))