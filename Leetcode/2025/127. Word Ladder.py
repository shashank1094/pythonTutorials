from functools import lru_cache
from typing import List

class Solution:
    # TIME LIMIT EXCEED
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     if endWord not in wordList:
    #         return 0
    #
    #     def is_valid_transformation(word, other_word):
    #         if not len(word) == len(other_word):
    #             return False
    #         diff = 0
    #         for char_index in range(len(word)):
    #             if not word[char_index] == other_word[char_index]:
    #                 diff += 1
    #         return diff == 1
    #
    #     def helper(curr_word, target_word, word_pool):
    #         if target_word not in word_pool:
    #             return float('inf')
    #         if is_valid_transformation(curr_word, target_word):
    #             return 1
    #
    #         min_cost = float('inf')
    #         for possible_word in word_pool:
    #             if is_valid_transformation(curr_word, possible_word):
    #                 cost = 1 + helper(possible_word, target_word, word_pool - {possible_word})
    #                 if cost < min_cost:
    #                     min_cost = cost
    #         return min_cost
    #
    #     number_of_transformation = helper(beginWord, endWord, set(wordList))
    #     return  0 if number_of_transformation == float('inf') else number_of_transformation + 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass

if __name__ == '__main__':
    print(Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
