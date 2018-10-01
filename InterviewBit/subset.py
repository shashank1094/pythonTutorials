# Given a set of distinct integers, S, return all possible subsets.
#
#  Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# Also, the subsets should be sorted in ascending ( lexicographic ) order.
# The list is not necessarily sorted.
# Example :
#
# If S = [1,2,3], a solution is:
#
# [
#   [],
#   [1],
#   [1, 2],
#   [1, 2, 3],
#   [1, 3],
#   [2],
#   [2, 3],
#   [3],
# ]

ans = [[]]


def helper(A, index):
    if index == len(A):
        return [[]]
    tmp = helper(A, index + 1)
    print('before tmp : {}'.format(tmp))
    r = []
    for i in tmp:
        t = [A[index]] + i
        r.append(t)
    print('result : {}'.format(r))
    tmp[1:1] = r
    print('after : {}'.format(tmp))
    return tmp


def subsets(A):
    A.sort()
    return helper(A, 0)


t = [1, 2, 3]
ans = subsets(t)
print(ans)
