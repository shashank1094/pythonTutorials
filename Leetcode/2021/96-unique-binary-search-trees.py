# https://leetcode.com/problems/unique-binary-search-trees/
from functools import lru_cache


class Solution:
    @lru_cache
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        total = 0
        for i in range(1, n + 1):
            total += self.numTrees(i - 1) * self.numTrees(n - i)
        return total


if __name__ == '__main__':
    print(Solution().numTrees(9))
