from collections import defaultdict
import random

class Solution:
    @staticmethod
    def is_vowel(character):
        return character in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def get_redundant_substrings_brute(self, word, a, b):
        n = len(word)
        redundant_count = 0
        for start_index in range(n):
            for end_index in range(start_index, n):
                sub_string = word[start_index:end_index+1]
                vowels = 0
                consonants = 0
                for current_index in range(len(sub_string)):
                    if self.is_vowel(sub_string[current_index]):
                        vowels += 1
                    else:
                        consonants += 1
                if a * vowels + b * consonants == len(sub_string):
                    redundant_count+=1
                    print(sub_string)
        return redundant_count

    def get_redundant_substrings(self, word, a, b):
        length_of_word = len(word)
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        vowels = 0
        consonants = 0
        redundant_count = 0
        for current_index in range(length_of_word):
            if self.is_vowel(word[current_index]):
                vowels+=1
            else:
                consonants+=1
            current_sum = a * vowels + b * consonants
            current_diff = current_sum - (current_index + 1)
            if current_diff in prefix_map:
                redundant_count += prefix_map[current_diff]
            prefix_map[current_sum]+=1
        return redundant_count



if __name__ == '__main__':
    print(Solution().get_redundant_substrings_brute("abbacci", -1, 2))
    print(Solution().get_redundant_substrings('abbacci', -1, 2))