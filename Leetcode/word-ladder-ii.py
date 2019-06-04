# https://leetcode.com/problems/word-ladder-ii/


class Solution:

    def __init__(self):
        self.options = {}
        self.ans = []
        self.first_found = False
        self.min_len_yet = float("inf")

    def pre_computation(self, word_list):
        for word in word_list:
            for index, value in enumerate(word):
                if index not in self.options:
                    self.options[index] = set()
                self.options[index].add(value)

    def findLadders(self, beginWord: str, endWord: str, word_list):
        self.pre_computation(word_list)
        if endWord not in word_list:
            return self.ans
        word_list = dict(zip(word_list, [True] * len(word_list)))
        self.util(beginWord, endWord, word_list, [])
        # final_ans = []
        # min = float("inf")
        # for x in self.ans:
        #     if len(x) < min:
        #         min = len(x)
        # return [x for x in self.ans if len(x) == min]
        return self.ans

    def util(self, a, z, word_list, curr_ans):
        curr_ans.append(a)
        if not word_list:
            return
        if len(curr_ans) > self.min_len_yet:
            return
        if a == z:
            if not self.first_found:
                self.first_found = True
            if len(curr_ans) <= self.min_len_yet:
                if len(curr_ans) < self.min_len_yet:
                    self.min_len_yet = len(curr_ans)
                    self.ans = []
                self.ans.append(curr_ans)
        for x in range(len(a)):
            for option in self.options.get(x, []):
                temp_a = a[:x] + option + a[x + 1:]
                if temp_a in word_list:
                    temp_curr_ans = curr_ans.copy()
                    temp_word_list_dict = word_list.copy()
                    temp_word_list_dict.pop(temp_a)
                    self.util(temp_a, z, temp_word_list_dict, temp_curr_ans)


if __name__ == '__main__':
    # for x in Solution().findLadders("qa", "sq",
    #                                 ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le",
    #                                  "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn",
    #                                  "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc",
    #                                  "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co",
    #                                  "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an",
    #                                  "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io",
    #                                  "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]):
    #     print(x, end="\n\n")
    for x in Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]):
        print(x, end="\n\n")
    pass
