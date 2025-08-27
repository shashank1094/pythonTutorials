# https://leetcode.com/problems/one-edit-distance/?envType=company&envId=stripe&favoriteSlug=stripe-thirty-days

class Solution:
    def isOneEditDistance(self, s: "str", t: "str") -> "bool":
        len_s, len_t = len(s), len(t)
        # Ensure that s is shorter than t.
        if len_s > len_t:
            return self.isOneEditDistance(t, s)
        # The strings are NOT one edit away from distance
        # if the length diff is more than 1.
        if len_t - len_s > 1:
            return False
        for i in range(len_s):
            if s[i] != t[i]:
                # If strings have the same length
                if len_s == len_t:
                    return s[i + 1 :] == t[i + 1 :]
                # If strings have different lengths
                else:
                    return s[i:] == t[i + 1 :]
        # If there are no diffs in ns distance
        # The strings are one edit away only if
        # t has one more character.
        return len_s + 1 == len_t

if __name__ == '__main__':
    print(Solution().isOneEditDistance('ab', 'abc'))
    print(Solution().isOneEditDistance('ab', 'a'))
    print(Solution().isOneEditDistance('abc', 'adc'))
    print(Solution().isOneEditDistance('cba', 'abc'))
