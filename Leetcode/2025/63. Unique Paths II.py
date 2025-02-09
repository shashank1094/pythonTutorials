# https://leetcode.com/problems/unique-paths-ii/description/
import copy
from typing import List

# Used backtracking in the solution but failed, because it is going recursively to each combination and is not needed,
# problem can be solved using dynamic programming.
# class Solution:
#
#     number_of_unique_paths = None
#     unique_paths = None
#
#     def helper(self, obstacle_grid, current_row, current_column, current_path):
#         if current_row == len(obstacle_grid) or current_column == len(obstacle_grid[0]):
#             return
#         if obstacle_grid[current_row][current_column] == 1:
#             return
#         if current_column == len(obstacle_grid[0])-1 and current_row == len(obstacle_grid)-1:
#             self.number_of_unique_paths+=1
#             self.unique_paths.append(copy.deepcopy(current_path))
#             return
#         valid_moves = [[0, 1], [1,0]]
#         for move in valid_moves:
#             next_row , next_column = move[0] + current_row, move[1] + current_column
#             current_path.append([next_row, next_column])
#             self.helper(obstacle_grid, next_row, next_column, current_path)
#             current_path.pop()
#
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         self.number_of_unique_paths = 0
#         self.unique_paths = []
#         self.helper(obstacleGrid, 0, 0, [])
#         print(self.unique_paths)
#         return self.number_of_unique_paths

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows= len(obstacleGrid)
        if not rows:
            return 0
        columns = len(obstacleGrid[0])
        if not columns:
            return 0
        dp_array = [[0 for _ in range(columns)] for _ in range(rows)]
        dp_array[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for row_index in range(1, rows):
            dp_array[row_index][0] = dp_array[row_index-1][0] if obstacleGrid[row_index][0] == 0 else 0
        for column_index in range(1, columns):
            dp_array[0][column_index] = dp_array[0][column_index-1] if obstacleGrid[0][column_index] == 0 else 0
        for row_index in range(1, rows):
            for column_index in range(1, columns):
                if obstacleGrid[row_index][column_index] == 1:
                    dp_array[row_index][column_index] = 0
                else:
                    dp_array[row_index][column_index] = dp_array[row_index-1][column_index] + dp_array[row_index][column_index-1]

        return dp_array[rows-1][columns-1]

if __name__ == "__main__":
    print(Solution().uniquePathsWithObstacles([[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]))