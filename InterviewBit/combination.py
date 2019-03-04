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
#  Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
# Example : itertools.combinations in python.
# If you do, we will disqualify your submission retroactively and give you penalty points.
# NOTE: You only need to implement the given function. Do not read input,
# instead use the arguments to the function. Do not print the output, instead return values as specified.
# Still have a doubt? Checkout Sample Codes for more details.


def sol(r1, r2, k):
    if k == 1:
        return [[i] for i in range(r1, r2)]
    if r1 == r2:
        return []
    if r2 - r1 < k:
        return []
    out = []
    for i in range(r1, r2):
        tr = sol(i + 1, r2, k - 1)
        for t in tr:
            out.append([i] + t)

    return out


def combine(n, k):
    return sol(1, n + 1, k)


print(combine(4, 2))
