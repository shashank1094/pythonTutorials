# Given n pairs of parentheses,
# write a function to generate all combinations of well-formed parentheses of length 2*n.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"
# Make sure the returned list of strings are sorted.
import math


# class Solution:
#
#     def __init__(self):
#         self.open_parenthesis = '('
#         self.closing_parenthesis = ')'
#         self.options = [self.open_parenthesis, self.closing_parenthesis]
#
#     def validate_parenthesis(self, test_string, n):
#         no_open_parenthesis = test_string.count(self.open_parenthesis)
#         no_close_parenthesis = test_string.count(self.closing_parenthesis)
#         ans = no_open_parenthesis <= no_close_parenthesis <= math.ceil(
#             n / 2) and no_open_parenthesis <= math.ceil(n / 2)
#         return ans
#
#     # @param n : integer
#     # @return a list of strings
#     def generateParenthesis(self, A):
#
#         def helper(tmp_size, real_size):
#             if tmp_size == 1:
#                 return self.closing_parenthesis
#             if tmp_size == 0:
#                 return
#
#             result = []
#             intermediate = helper(tmp_size - 1, real_size)
#             for temp_res in intermediate:
#                 for option in self.options:
#                     if self.validate_parenthesis(option + temp_res, real_size):
#                         result.append(option + temp_res)
#
#             return result
#
#         return sorted(helper(2 * A, 2 * A))
#
#
# if __name__ == '__main__':
#     sol1 = Solution()
#     print(len(sol1.generateParenthesis(14)))


class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, n):
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left, right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        if right < left:
            return
        if not left and not right:
            ans.append(string)
            return
        if left:
            self.dfs(left - 1, right, ans, string + "(")
        if right:
            self.dfs(left, right - 1, ans, string + ")")


if __name__ == '__main__':
    sol2 = Solution()
    print('\n'.join(sol2.generateParenthesis(5)))
