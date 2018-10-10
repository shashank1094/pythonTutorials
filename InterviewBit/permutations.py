# Given a collection of numbers, return all possible permutations.
#
# Example:
#
# [1,2,3] will have the following permutations:
#
# [1,2,3]
# [1,3,2]
# [2,1,3]
# [2,3,1]
# [3,1,2]
# [3,2,1]
#  NOTE
# No two entries in the permutation sequence should be the same.
# For the purpose of this problem, assume that all the numbers in the collection are unique.


# class Solution:
#     # @param l1 : list of integers
#     # @return a list of list of integers
#     @staticmethod
#     def permute(l1):
#         def helper(options, index):
#             if index == len(options) - 1:
#                 return [[option] for option in options]
#             intermediate = helper(options, index + 1)
#             result = []
#             for opt in options:
#                 for res in intermediate:
#                     if opt not in res:
#                         result.append([opt] + res)
#
#             return result
#
#         return sorted(helper(sorted(l1), 0))
#
#
# if __name__ == '__main__':
#     sol1 = Solution()
#     print(sol1.permute(list(range(10))))


class Solution:
    # @param arr : list of integers
    # @return a list of list of integers
    def permute(self, arr):
        res = []
        l = 0
        r = len(arr) - 1
        self.permutation_helper(arr, res, l, r)
        res.sort()
        return res

    def permutation_helper(self, arr, res, l, r):

        if l == r:
            res.append(arr[:])

        else:
            for i in range(l, r + 1):
                arr[l], arr[i] = arr[i], arr[l]
                self.permutation_helper(arr, res, l + 1, r)
                arr[l], arr[i] = arr[i], arr[l]


if __name__ == '__main__':
    sol2 = Solution()
    num = 1
    for i in sol2.permute(list(range(1, 5))):
        print(i, num)
        num += 1
