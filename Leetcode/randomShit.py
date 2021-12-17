#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumSwaps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY popularity as parameter.
#

def minimumSwaps(popularity):
    # Write your code here
    n = len(popularity)
    arr_pos = [*enumerate(popularity)]
    arr_pos.sort(key=lambda x: x[1], reverse=True)
    vis = {x: False for x in range(n)}
    ans = 0
    for i in range(n):
        if vis[i] or arr_pos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arr_pos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans


if __name__ == '__main__':
    print(minimumSwaps([3, 4, 62, 4, 8, 4, 2]))
