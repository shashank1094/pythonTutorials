from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        def hide_unsurrounded_region(x, y):
            if 0 <= x < rows and 0 <= y < cols and board[x][y] == 'O':
                board[x][y] = '1'
                hide_unsurrounded_region(x + 1, y)
                hide_unsurrounded_region(x - 1, y)
                hide_unsurrounded_region(x, y + 1)
                hide_unsurrounded_region(x, y - 1)

        for i in range(rows):
            hide_unsurrounded_region(i, 0)
            hide_unsurrounded_region(i, cols - 1)

        for j in range(cols):
            hide_unsurrounded_region(0, j)
            hide_unsurrounded_region(rows - 1, j)

        import pprint
        pprint.pprint(board)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '1':
                    board[i][j] = 'O'
        pprint.pprint(board)


if __name__ == '__main__':
    Solution().solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
