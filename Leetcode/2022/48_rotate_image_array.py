# https://leetcode.com/problems/rotate-image/

array = list(range(101, 111))

index = 9
while index >= 0:
    print(array[index], index, bin(index), array[~index], ~index,
          bin(~index))
    index -= 1


