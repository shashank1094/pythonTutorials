from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.ans = []
        self.helper(S, 0, "")
        return self.ans

    def helper(self, inp, index, curr):
        if index == len(inp):
            self.ans.append(curr)
            return
        self.helper(inp, index + 1, curr + inp[index].lower())
        if inp[index].isalpha():
            self.helper(inp, index + 1, curr + inp[index].upper())


if __name__ == '__main__':
    print(Solution().letterCasePermutation('a1b2'))
