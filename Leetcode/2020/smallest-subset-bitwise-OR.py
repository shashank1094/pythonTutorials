from functools import reduce


def Get_minimum(A):
    A = list(A)
    final = reduce(lambda a, b: a | b, A)
    min_size = float("inf")
    max_ans = float("-inf")
    n = len(A)
    for i in range(1,n):
        for j in range(n-i):
            ans = reduce(lambda a, b: a | b, A[j:j+i])
            if ans > max_ans:
                max_ans = ans
                min_size = i
            if ans == max_ans:
                if i < min_size:
                    min_size = i
            if ans == final:
                print(final)
                print(max_ans)
                print(min_size)
                return min_size
    print(final)
    print(max_ans)
    print(min_size)
    return min_size


T = 1
for _ in range(T):
    n = 5
    import random

    A = random.sample(range(1, 10784), 34)
    out_ = Get_minimum(A)
    print (out_)