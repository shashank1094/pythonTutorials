"""
abcdxyz
xyzabcd
yabcd
out:
abcd

"""


# def longest_common_substring(str1, str2):
#     if len(str1) < len(str2):
#         smaller_str = str1
#         other_str = str2
#     else:
#         smaller_str = str2
#         other_str = str1
#
#     win_size = len(smaller_str)
#     while win_size > 0:
#         for index in range(0, len(smaller_str) - win_size + 1):
#             sub_str = smaller_str[index:index + win_size]
#             if sub_str in other_str:
#                 return sub_str
#         win_size -= 1
#     return

def longest_common_substring(str1, str2):
    if len(str1) < len(str2):
        smaller_str = str1
        other_str = str2
    else:
        smaller_str = str2
        other_str = str1
    memo = {}

    win_size = 1
    _max = ''
    while win_size < len(smaller_str) + 1:
        for index in range(0, len(smaller_str) - win_size + 1):
            matches = False
            sub_str = smaller_str[index:index + win_size]
            one_less_substr = sub_str[:-1]
            if one_less_substr in memo:
                _start, _end = memo[one_less_substr]
                if _end+1 < len(other_str) and sub_str[-1] == other_str[_end+1]:
                    matches = True
                    memo[sub_str] = (index, index + win_size - 1)
            if not matches:
                _start = None
                try:
                    _start = other_str.index(sub_str)
                except:
                    pass
                if _start is not None:
                    matches = True
                    memo[sub_str] = (_start, _start + win_size -1)
            if matches and len(_max) < len(sub_str):
                _max=sub_str
            # print(_max, index, sub_str, memo,other_str)
        win_size += 1
    return _max


if __name__ == '__main__':
    print(longest_common_substring('abcdpqrstxyz', 'xyzpqrstabcd'))
