dp = {}


def Solve(N):
    # Write your code here
    # Return your answer
    mod_by = 10**9+7
    from math import ceil, log
    h = ceil(log(N + 1, 2)) - 1
    total = 0
    for i in range(h, 0, -1):
        nn = 2 ** (h - i)
        total += util(i) * nn
    return total % mod_by


def util(h):
    if h in dp:
        return dp[h]
    sum = 0
    nodes_till_now = 1
    for x in range(1, h + 1):
        nn = 2 ** x
        sum += x * nn
    dp[h] = sum
    return sum


T = 1

for _ in range(T):
    N = 4

    out_ = Solve(N)

    print(out_)