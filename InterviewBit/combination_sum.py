# Given a set of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
#  Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The combinations themselves must be sorted in ascending order.
# CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR …
# (a1 = b1 AND a2 = b2 AND … ai = bi AND ai+1 > bi+1)
# The solution set must not contain duplicate combinations.
# Example,
# Given candidate set 2,3,6,7 and target 7,
# A solution set is:
#
# [2, 2, 3]
# [7]
#  Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
# Example : itertools.combinations in python.
# If you do, we will disqualify your submission retroactively and give you penalty points.


def combination_helper(choices, target, ans, tmp_result, index):
    if target < 0:
        return
    if target == 0:
        ans.append(sorted(tmp_result[:]))
        return
    while index <= len(choices) - 1 and target - choices[index] >= 0:
        tmp_result.append(choices[index])
        combination_helper(choices, target - choices[index], ans, tmp_result, index)
        tmp_result.pop()
        index += 1


def combination_sum(c, t):
    ans = []
    c = sorted(list(set(c)))
    combination_helper(c, t, ans, [], 0)
    return sorted(ans)


print(combination_sum([2, 3, 6, 7], 15))
