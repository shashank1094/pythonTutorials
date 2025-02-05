# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from importlib.abc import SourceLoader
from typing import List


class Solution:
    digit_letter_mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def helper(self, digits, current_combination ,letter_combinations):
        if not len(digits):
            if current_combination:
                letter_combinations.append(current_combination)
            return
        digit = digits[0]
        for letter in self.digit_letter_mapping[digit]:
            current_combination+=letter
            self.helper(digits[1:], current_combination, letter_combinations)
            current_combination = current_combination[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        letter_combinations = []
        self.helper(digits, "", letter_combinations)
        return letter_combinations

if __name__ == '__main__':
    print(Solution().letterCombinations("23"))