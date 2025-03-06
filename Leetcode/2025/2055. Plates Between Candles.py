from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, qs: List[List[int]]) -> List[int]:
        n = len(s)
        prefcandle = [-1] * n  # this stores the position of closest candle from current towards left
        suffcandle = [0] * n  # this stores the position of closest candle from current towards right

        pref = [0] * n  # stores the number of plates  till ith position from 0 - for i = 0 -> n

        ind = -1
        c = 0
        # The following method calculates number of plates(*) till ith position from 0 - for i = 0 -> n
        for i in range(n):
            if ind != -1 and s[i] == '*':
                c += 1
            elif s[i] == '|':
                ind = i
            pref[i] = c

        # this method calculates the left nearest candle to a point
        # intial is -1 as to left of leftmost element no candle can be present
        ind = -1
        for i in range(n):
            if s[i] == '|':
                ind = i
            prefcandle[i] = ind

        # this method calculates the right nearest candle to a point
        # intial is infinity as to right of rightmost element no candle can be present
        ind = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                ind = i
            suffcandle[i] = ind

        # m = no of queries
        m = len(qs)
        ans = [0] * m

        for i in range(m):
            c = 0
            l = qs[i][0]
            r = qs[i][1]

            # check if left nearest candle of right boundary is after left boundary
            # check if right nearest candle of left boundary is before right boundary
            # to summarise - here we find if there is a pair of candle present within the given range or not
            if prefcandle[r] < l or suffcandle[l] > r:
                continue

            # desired answer is no of pplates(*) only inside 2 candles (|) inside the given boundary area
            ans[i] = pref[prefcandle[r]] - pref[suffcandle[l]]
        return ans


if __name__ == '__main__':
    print(Solution().platesBetweenCandles(s = "**|**|***|", qs = [[2,5],[5,9]]))