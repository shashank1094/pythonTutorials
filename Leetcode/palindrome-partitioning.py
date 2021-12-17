# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s):
        self.ans = []
        self.util(s, 0, len(s), [])
        return self.ans

    def util(self, s, start, end, curr):
        # if end == len(s):
        #     self.ans.append(curr)
        if start == end:
            self.ans.append(curr[:])
            return
        for x in range(start, end):
            if self.is_palindrome(s[start:x + 1]):
                self.util(s, x + 1, end, curr + [s[start:x + 1]])

    def is_palindrome(self, s):
        return all([s[x] == s[~x] for x in range(len(s) // 2)])


if __name__ == '__main__':
    print(Solution().partition('nitin'))
