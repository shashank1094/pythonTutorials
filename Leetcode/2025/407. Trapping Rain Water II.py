# https://leetcode.com/problems/trapping-rain-water-ii/description/
import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        boundaries = []
        water_trapped = 0
        rows = len(heightMap)
        cols = len(heightMap[0]) if rows else 0
        if not rows or not cols:
            return water_trapped
        visited = [[False] * cols for _ in range(rows)]
        for row_index in range(rows):
            for col_index in range(cols):
                if row_index == 0 or col_index == 0 or row_index == rows - 1 or col_index == cols - 1:
                    heapq.heappush(boundaries, (heightMap[row_index][col_index], row_index, col_index))
                    visited[row_index][col_index] = True
        while len(boundaries):
            curr_height, curr_row, curr_col = heapq.heappop(boundaries)
            for neighbor_row_diff, neighbor_col_diff in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                neighbor_row = curr_row + neighbor_row_diff
                neighbor_col = curr_col + neighbor_col_diff
                if -1 < neighbor_col < cols and -1 < neighbor_row < rows and not visited[neighbor_row][neighbor_col]:
                    if heightMap[neighbor_row][neighbor_col] < curr_height:
                        water_trapped += curr_height - heightMap[neighbor_row][neighbor_col]
                        heapq.heappush(boundaries, (curr_height, neighbor_row, neighbor_col))
                        visited[neighbor_row][neighbor_col] = True
                    else:
                        heapq.heappush(boundaries, (heightMap[neighbor_row][neighbor_col], neighbor_row, neighbor_col))
                        visited[neighbor_row][neighbor_col] = True
        return water_trapped


if __name__ == '__main__':
    print(Solution().trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))
    print(
        Solution().trapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))
    print(Solution().trapRainWater([[1, 2, 3, 4, 5], [2, 0, 0, 0, 1], [1, 0, 0, 0, 2], [4,3,2,1,3]]))