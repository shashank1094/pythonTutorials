# https://docs.python.org/3/library/collections.html#deque-objects
from collections import deque


def roundrobin(*iterables):
    iterators = deque(map(iter, iterables))
    # print(iterators)
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
                # print(iterators)
        except StopIteration:
            # Remove an exhausted iterator.
            iterators.popleft()


print(list(roundrobin('ABC', 'D', 'EF')))

l = [1, 2, 3, 4, 'a']
dl = deque(l)
dl.rotate(2)
print(dl)
