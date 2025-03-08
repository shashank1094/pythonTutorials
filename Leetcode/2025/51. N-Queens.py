# https://leetcode.com/problems/n-queens/description/
import copy
from typing import List


class Solution:
    all_solution_boards = []

    def helper_method(self, row_index, occupied_columns, occupied_diagonals, occupied_anti_diagonal, current_board):
        if row_index == len(current_board):
            temp_board = copy.deepcopy(current_board)
            for temp_row in range(len(temp_board)):
                temp_board[temp_row] = "".join(temp_board[temp_row])
            self.all_solution_boards.append(temp_board)

        for column_index in range(len(current_board)):
            diagonal = row_index - column_index
            anti_diagonal = row_index + column_index
            if column_index in occupied_columns or diagonal in occupied_diagonals or anti_diagonal in occupied_anti_diagonal:
                continue
            current_board[row_index][column_index] = "Q"
            occupied_columns.add(column_index)
            occupied_diagonals.add(diagonal)
            occupied_anti_diagonal.add(anti_diagonal)
            self.helper_method(row_index + 1, occupied_columns, occupied_diagonals, occupied_anti_diagonal,
                               current_board)
            current_board[row_index][column_index] = "."
            occupied_columns.remove(column_index)
            occupied_diagonals.remove(diagonal)
            occupied_anti_diagonal.remove(anti_diagonal)

    def solveNQueens(self, n: int) -> List[List[str]]:
        initial_board = [['.']*n for _ in range(n)]
        self.helper_method(
            row_index=0,
            occupied_columns=set(),
            occupied_diagonals=set(),
            occupied_anti_diagonal=set(),
            current_board=initial_board
        )
        return self.all_solution_boards


if __name__ == '__main__':
    for _row in Solution().solveNQueens(4):
        print(_row)
