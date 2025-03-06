# https://leetcode.com/problems/number-of-islands/description/
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_islands = 0
        if len(grid) == 0 or len(grid[0]) == 0:
            return num_of_islands
        rows = len(grid)
        cols = len(grid[0])
        visited_map = [[False]*cols for _ in range(rows)]
        stack = deque()
        for row_index in range(rows):
            for col_index in range(cols):
                if visited_map[row_index][col_index]:
                    continue
                if grid[row_index][col_index] == '1':
                    stack.append((row_index, col_index))
                    num_of_islands+=1
                while len(stack):
                    row, col = stack.pop()
                    if visited_map[row][col]:
                        continue
                    visited_map[row][col] = True
                    if row+1 < rows and grid[row+1][col] == '1':
                        stack.append((row + 1, col))
                    if col+1 < cols and grid[row][col+1] == '1':
                        stack.append((row, col+1))
                    if row-1 >= 0 and grid[row-1][col] == '1':
                        stack.append((row - 1, col))
                    if col-1 >= 0 and grid[row][col-1] == '1':
                        stack.append((row, col-1))
        return num_of_islands


if __name__ == '__main__':
    print(Solution().numIslands(
        [["1", "1", "1", "1", "0"],
         ["1", "1", "0", "1", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "0", "0", "1"]]))