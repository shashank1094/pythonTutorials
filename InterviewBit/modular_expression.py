# Implement pow(A, B) % C.
#
# In other words, given A, B and C,
# find (A^B)%C.
#
# Input : A = 2, B = 3, C = 3
# Return : 2
# 2^3 % 3 = 8 % 3 = 2
#
# (M * N) % P = (M % P * N % P) % P


def mod(m, n, p):
    if n == 0:
        return 1 % p  # What if p is 1
    elif n % 2 == 0:
        y = mod(m, n / 2, p)
        return (y * y) % p
    else:
        return (m % p) * (mod(m, n - 1, p)) % p


print(mod(2, 3, 3))
