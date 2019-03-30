# n = int(input())
#
# a = [int(x) for x in input().split(sep=" ", maxsplit=n)]
#
# print(a)


# import re
#
# sentence = 'horses are fast'
# regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
# matched = re.search(regex, sentence)
# print(matched.groupdict())

def f(arr, k):
    um = {}
    sum = 0
    maxLen = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum == k:
            maxLen = i + 1
        if sum-k in um:
            maxLen = i - um[sum - k]
        else:
            um[sum] = i

    return maxLen

print(f([11,2,-2,3], 0))
