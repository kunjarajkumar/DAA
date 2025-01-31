class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def is_safe(board, row, col):
            # Check if placing the queen at (row, col) is safe
            for i in range(row):
                # Check column and diagonals
                if board[i] == col or \
                   board[i] - i == col - row or \
                   board[i] + i == col + row:
                    return False
            return True

        def solve(board, row):
            # If all queens are placed, add the board configuration to results
            if row == n:
                result.append(['.' * i + 'Q' + '.' * (n - i - 1) for i in board])
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col  # Place queen
                    solve(board, row + 1)  # Recur for the next row
                    board[row] = -1  # Backtrack

        result = []
        solve([-1] * n, 0)  # Initialize the board and start solving from the first row
        return result
