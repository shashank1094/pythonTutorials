"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.

"""
from collections import OrderedDict


class Solution(object):
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """

        character_frequency = OrderedDict()
        for index in range(len(s)):
            c = s[index]
            character_frequency[c] = ((character_frequency.get(c, (0, -1)))[0] + 1, index)
        for k, v in character_frequency.items():
            if v[0] == 1:
                return v[1]
        return -1


if __name__ == '__main__':
    print(Solution().firstUniqChar('loveleetcode'))
