class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str word / sentence in which the longest palindrome is to be found.
        :rtype: str longest sub-sting which is palindrome.
        """
        input_string = s
        longest_palindrome = input_string[0]

        # 2 D array in which row i, column j represent
        # whether s[i:j+1] is a palindrome or not
        previous_memory = [[0 for _ in range(len(input_string))] for _ in range(len(input_string))]

        def print_2d_array():
            for _index in range(len(input_string)):
                print(previous_memory[_index])

        # print_2d_array()

        for start in range(len(input_string)-1, -1, -1):
            for end in range(start, len(input_string)):
                if start == end:
                    previous_memory[start][end] = True
                    continue
                if input_string[start] == input_string[end]:
                    # If the substring between two indexes is a palindrome or
                    # the substring of type aa bb cc, etc...
                    if previous_memory[start+1][end-1] or end - start == 1:
                        previous_memory[start][end] = True
                        if len(input_string[start:end+1]) > len(longest_palindrome):
                            longest_palindrome = input_string[start:end+1]
                # print(start, end, input_string[start:end + 1])
                # print_2d_array()
        return longest_palindrome

if __name__ == '__main__':
    print("Answer :: ", Solution().longestPalindrome("ecbbcd"))
    print("Answer :: ", Solution().longestPalindrome("racecar"))
    # print([i for i in range(6, -1, -1 )][0:2])~