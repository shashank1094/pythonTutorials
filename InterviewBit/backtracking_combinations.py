# Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.
#
# Make sure the combinations are sorted.
#
# To elaborate,
#
# Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
# Entries should be sorted within themselves.
# Example :
# If n = 4 and k = 2, a solution is:
#
# [
#   [1,2],
#   [1,3],
#   [1,4],
#   [2,3],
#   [2,4],
#   [3,4],
# ]


class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        return self.sol(1, A + 1, B)

    def sol(self, start, end, k):
        if k == 1:
            return [[i] for i in range(start, end)]
        if start == end:
            return []
        if end - start < k:
            return []
        output = []
        for i in range(start, end):
            tr = self.sol(i + 1, end, k - 1)
            for t in tr:
                output.append([i] + t)

        return output


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
