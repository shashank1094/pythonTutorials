from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        self.ans = []
        self.hour_options = [1, 2, 4, 8]
        self.minute_options = [1, 2, 4, 8, 16, 32]
        self.helper(num)
        return self.ans

    def helper(self, num, curr_h, curr_m):
        if num == 0:
            if curr_h <= 11 and curr_m <= 59:
                self.ans.append("{}:{:0>2}".format(curr_h, curr_m))
        # 4 choices
        self.helper(num - 1, )
