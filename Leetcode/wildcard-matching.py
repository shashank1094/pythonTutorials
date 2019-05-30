# https://leetcode.com/problems/wildcard-matching/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.dp = {}
        return self.util(s, p, 0, 0)

    def util(self, s, p, s_start, p_start):
        dp_str = str(s_start) + ":" + str(p_start)
        if dp_str in self.dp:
            return self.dp[dp_str]

        if s_start == len(s) and p_start == len(p):
            self.dp[dp_str] = True
            return True

        if p_start == len(p):
            self.dp[dp_str] = False
            return False

        ans = False

        if p[p_start] == '*':
            ans = self.util(s, p, s_start, p_start + 1) \
                   or (self.util(s, p, s_start + 1, p_start) if s_start < len(s) else False)\
                   or (self.util(s, p, s_start + 1, p_start+1) if s_start < len(s) else False)

        if s_start < len(s) and (p[p_start] == '?' or s[s_start] == p[p_start]):
            ans = self.util(s, p, s_start + 1, p_start + 1)

        self.dp[dp_str] = ans

        return ans


if __name__ == '__main__':
    print(Solution().isMatch("a", "a*"))
