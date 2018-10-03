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


def helper(li, index):
    print('lis : {}, index : {}'.format(li, index))
    if index == len(li):
        return [[]]
    tmp = helper(li, index + 1)
    print('before tmp : {}'.format(tmp))
    r = []
    for i in tmp:
        t = [li[index]] + i
        r.append(t)
    print('result : {}'.format(r))
    tmp[1:1] = r
    print('after tmp: {}'.format(tmp))
    print('DONE lis : {}, index : {}'.format(li, index))
    return tmp


def subsets(l1):
    l1.sort()
    return helper(l1, 0)


t = [1, 2, 3]
ans = subsets(t)
print(ans)
