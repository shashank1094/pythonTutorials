# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
#
#
# The digit 0 maps to 0 itself.
# The digit 1 maps to 1 itself.
#
# Input: Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Make sure the returned strings are lexicographically sorted.
#
#  NOTE: You only need to implement the given function. Do not read input, instead use the arguments to the function.
#  Do not print the output, instead return values as specified.
#  Still have a doubt? Checkout Sample Codes for more details.


ans = [[]]


class Solution:
    phone = {'0': ['0'],
             '1': ['1'],
             '2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    def comb_helper(self, s):
        global ans
        for index in range(len(s)):
            tmp = []
            for tmp_ans in ans[:]:
                for option in self.phone[s[index]]:
                    tmp.append(tmp_ans + [option])
            ans = tmp

    def letter_combinations(self, s1):
        global ans
        self.comb_helper(s1)
        ans = [''.join(x) for x in ans]
        return ' '.join(ans)


if __name__ == '__main__':
    sol1 = Solution()
    print(sol1.letter_combinations('23'))


class Solution:

    def __init__(self):
        self.digitToLetters = {
            "0": "0",
            "1": "1",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    def letter_combinations(self, l1):
        if len(l1) == 0:
            return []
        elif len(l1) == 1:
            return list(self.digitToLetters[l1])
        else:
            res = []

            intermediate = self.letter_combinations(l1[1:])
            for first in self.digitToLetters[l1[0]]:
                for rest in intermediate:
                    res.append(first + rest)

            return res


if __name__ == '__main__':
    sol2 = Solution()
    print(sol2.letter_combinations('234'))
