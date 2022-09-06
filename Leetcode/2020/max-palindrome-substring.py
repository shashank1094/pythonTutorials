from collections import defaultdict


def frequency(s):
    freq = defaultdict(int)
    for i in s:
        freq[i]+=1
    return freq

def subtract_freq(f1,f2, options):
    for x in options:
        if f1[x] - f2 [x] >=0:
            f1[x]-=f2[x]
        else:
            return 0
    return 1

def Solve(SL, PL, S, P):
    freq_s = frequency(S)
    freq_p = frequency(P)
    n = 0
    while subtract_freq(freq_s, freq_p, set(P)):
        n+=1
    return n

# write your code here
# return your answer


# SL, PL = map(int, input().split())
#
# S = input()
#
# P = input()

out_ = Solve(10, 4, 'abcbbcabcc', 'bccb')

print(out_)