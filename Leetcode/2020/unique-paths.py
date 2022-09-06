# https://leetcode.com/problems/unique-paths/submissions/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [0] * n
        for row in range(n - 1, -1, -1):
            temp = [0] * m
            for col in range(m - 1, -1, -1):
                ans[row] = temp
                if col == m - 1:
                    ans[row][col] = 1
                elif row == n - 1:
                    ans[row][col] = 1
                else:
                    ans[row][col] = ans[row + 1][col] + ans[row][col + 1]
        return ans[0][0]
