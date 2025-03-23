# https://leetcode.com/problems/rotate-image/description/
from typing import List


class Solution:
    def print_2d_array(self, matrix):
        for row in matrix:
            print(row)

    def rotate(self, matrix: List[List[int]]) -> None:
        print("Original Matrix")
        self.print_2d_array(matrix)
        self.transpose(matrix)
        print("Transposed Matrix")
        self.print_2d_array(matrix)
        self.reflect(matrix)
        print("Rotated Matrix")
        self.print_2d_array(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n -j - 1] = (
                    matrix[i][n -j - 1],
                    matrix[i][j],
                )


if __name__ == '__main__':
    original_array= [[1,2,3],
                     [4,5,6],
                     [7,8,9]]

    Solution().rotate(original_array)
