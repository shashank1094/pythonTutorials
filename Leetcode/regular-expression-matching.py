# https://leetcode.com/problems/regular-expression-matching/


class Solution:

    def __init__(self):
        self.dp = None

    def isMatch(self, s, p):
        # Initialization of DP array.
        self.dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        # print(self.dp)
        self.dp[0][0] = True

        for i in range(2, len(p) + 1):
            self.dp[0][i] = self.dp[0][i-2] and p[i - 1] == '*'

        # print(self.dp)

        for j in range(1, len(s) + 1):
            for i in range(1, len(p) + 1):
                p_char = p[i-1]
                s_char = s[j-1]
                if p_char == "*":
                    self.dp[j][i] = self.dp[j][i-2]
                    if not self.dp[j][i]:
                        if p[i-2] == s_char or p[i-2] == ".":
                            self.dp[j][i] = self.dp[j-1][i]
                elif p_char == s_char or p_char == ".":
                    self.dp[j][i] = self.dp[j-1][i-1]
                else:
                    self.dp[j][i] = False

        # print(self.dp)
        return self.dp[len(s)][len(p)]


if __name__ == '__main__':
    print(Solution().isMatch("xaabyc", ".*"))
