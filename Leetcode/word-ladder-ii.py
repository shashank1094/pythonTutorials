# https://leetcode.com/problems/word-ladder-ii/


class Solution:

    def __init__(self):
        self.options = {}
        self.ans = []

    def pre_computation(self, word_list):
        for word in word_list:
            for index, value in enumerate(word):
                if index not in self.options:
                    self.options[index] = set()
                self.options[index].add(value)

    def findLadders(self, beginWord: str, endWord: str, wordList):
        self.pre_computation(wordList)
        if endWord not in wordList:
            return self.ans
        self.util(beginWord, endWord, wordList, [])
        final_ans = []
        min = float("inf")
        for x in self.ans:
            if len(x) < min:
                min = len(x)
        return [x for x in self.ans if len(x) == min]

    def util(self, a, z, word_list, curr_ans):
        curr_ans.append(a)
        if not word_list:
            return
        if a == z:
            self.ans.append(curr_ans)
        for x in range(len(a)):
            for option in self.options[x]:
                temp_a = a[:x] + option + a[x + 1:]
                if temp_a in word_list:
                    temp_curr_ans = curr_ans.copy()
                    temp_word_list = word_list.copy()
                    temp_word_list.remove(temp_a)
                    self.util(temp_a, z, temp_word_list, temp_curr_ans)


if __name__ == '__main__':
    for x in Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]):
        print(x, end="\n\n")
