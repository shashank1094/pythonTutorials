# https://leetcode.com/problems/coin-change/description/
import math
from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        def countComb(target, current_index):
            if current_index >= len(coins) or target < 0:
                return float('inf')  # No valid solution
            if target == 0:
                return 0  # No coins needed

            not_pick = countComb(target, current_index + 1)
            pick = 1 + countComb(target - coins[current_index], current_index)
            return min(pick, not_pick)

        answer = countComb(amount, 0)
        return answer if answer != float('inf') else -1


class SolutionMemo:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def coinChangeInner(rem):
            if rem < 0:
                return math.inf
            if rem == 0:
                return 0
            if rem in cache:
                return cache[rem]

            cache[rem] = min(coinChangeInner(rem - x) + 1 for x in coins)
            return cache[rem]

        ans = coinChangeInner(amount)
        return -1 if ans == math.inf else ans

    # Time Limit Exceeded

if __name__ == '__main__':
    # print(Solution().coinChange([436,405, 7, 3], 8379))
    print(SolutionMemo().coinChange([436, 405, 7, 3], 8379))
