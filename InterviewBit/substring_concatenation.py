import re


class Solution:
    # @param s : string
    # @param l : tuple of strings
    # @return a list of integers
    def findSubstring(self, s, l):
        ans = []
        l = list(l)
        l.sort()
        jump = len(l[0])
        jump_regex = '.{' + str(jump) + '}'
        chunk = jump * len(l)
        index = 0
        while index < len(s):
            initial_chunk = s[index:index + jump]
            if initial_chunk in l:
                chunk_to_be_checked = s[index:index + chunk]
                if len(chunk_to_be_checked) == chunk:
                    temp_l = re.findall(jump_regex, chunk_to_be_checked)
                    temp_l.sort()
                    if temp_l == l:
                        ans.append(index)
            index += 1

        return ans


if __name__ == '__main__':
    sol1 = Solution()
    print(sol1.findSubstring('barfoobarthefoobarman', ["foo", "bar"]))
