# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        n = len(string)
        if n < 1:
            return 0
        cur_len = 1  # To store the length of current substring
        max_len = 1  # To store the result
        i = 0
        start = 0

        # Initialize the visited array as -1, -1 is used to indicate
        # that character has not been visited yet.
        visited = {}

        # Mark first character as visited by storing the index of
        # first character in visited array.

        visited[string[0]] = 0
        # Start from the second character. First character is already
        # processed (cur_len and max_len are initialized as 1, and
        # visited[str[0]] is set
        for i in range(1, n):
            prev_index = visited.get(string[i], -1)

            # If the current character is not present in the already
            # processed substring or it is not part of the current NRCS,
            # then do cur_len++
            if prev_index == -1 or (i - cur_len > prev_index):
                cur_len += 1

            # If the current character is present in currently considered
            # NRCS, then update NRCS to start from the next character of
            # previous instance.
            else:
                # Also, when we are changing the NRCS, we should also
                # check whether length of the previous NRCS was greater
                # than max_len or not.
                if cur_len > max_len:
                    max_len = cur_len
                    start = i - cur_len

                cur_len = i - prev_index

            # update the index of current character
            visited[string[i]] = i

        # Compare the length of last NRCS with max_len and update
        # max_len if needed
        if cur_len > max_len:
            max_len = cur_len
            start = i - cur_len

        print(string[start:start + max_len])
        return max_len


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("GEEKSFORGEEKS"))
