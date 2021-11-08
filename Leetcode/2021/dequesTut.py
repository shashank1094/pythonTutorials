# time_append.py

from collections import deque
from time import perf_counter

TIMES = 10_000
a_list = []
a_deque = deque()


def average_time(func, times):
    total = 0.0
    for i in range(times):
        start = perf_counter()
        func(i)
        total += (perf_counter() - start) * 1e9
    return total / times


a_list = [TIMES] * TIMES
for _ in range(TIMES):
    a_deque.append(TIMES)

print(f'len() : {len(a_list)}')
list_time = average_time(lambda i: a_list.pop(0), TIMES)
deque_time = average_time(lambda i: a_deque.popleft(), TIMES)
print(f'len() : {len(a_list)}')
gain = list_time / deque_time

print(f"list.insert()      {list_time:.6} ns")
print(f"deque.appendleft() {deque_time:.6} ns  ({gain:.6}x faster)")
