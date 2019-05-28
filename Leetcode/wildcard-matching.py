# https://leetcode.com/problems/wildcard-matching/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = self.remove_consecutive(p)
        return self.util(s, p, 0, 0)

    def remove_consecutive(self, p):
        import re
        p = re.sub('\*{1,}', '*', p)
        return p

    def util(self, s, p, s_start, p_start):
        if s_start == len(s) and p_start == len(p):
            return True
        if p_start == len(p):
            return False
        if p[p_start] == '*':
            return self.util(s, p, s_start, p_start + 1) \
                   or (self.util(s, p, s_start + 1, p_start) if s_start < len(s) else False)
        if s_start >= len(s):
            return False
        if p[p_start] == '?' or s[s_start] == p[p_start]:
            return self.util(s, p, s_start + 1, p_start + 1)
        return False


if __name__ == '__main__':
    print(Solution().isMatch(
        "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb",
        "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"))
