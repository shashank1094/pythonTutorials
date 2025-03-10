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

if __name__ == '__main__':
    print(Solution().longestValidParentheses('))()()))()'))
    print(SolutionImproved().longestValidParentheses('))()()))()'))