from itertools import cycle, islice
from string import ascii_lowercase


def gen(x, n):
    c = cycle(x)
    while True:
        yield list(islice(c, n))


G = gen(ascii_lowercase, 100)

print(next(G))  # ['a', 'b', 'c', 'd', 'e']
print(next(G))  # ['f', 'g', 'h', 'i', 'j']
print(next(G))
print(next(G))
print(next(G))  # ['u', 'v', 'w', 'x', 'y']
print(next(G))  # ['z', 'a', 'b', 'c', 'd']
print(next(G))
print(next(G))
