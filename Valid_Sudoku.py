from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Check whether a partially filled 9x9 Sudoku board is valid.

        Rules:
        - Each row must not contain duplicates.
        - Each column must not contain duplicates.
        - Each 3x3 sub-box must not contain duplicates.
        """
        cols = defaultdict(set)
        rows = defaultdict(set)
        subbox = defaultdict(set)

        for r in range(9):
            for c in range(9):
                # Skip empty cells
                if board[r][c] == '.':
                    continue

                # If the value already exists in the row, column, or box, invalid board
                if (
                    board[r][c] in cols[c] or
                    board[r][c] in rows[r] or
                    board[r][c] in subbox[(r // 3, c // 3)]
                ):
                    return False

                # Add value to row, column, and sub-box tracking sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                subbox[(r // 3, c // 3)].add(board[r][c])

        return True


# Test cases inside the code
sol = Solution()

board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(sol.isValidSudoku(board1))  # True

board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(sol.isValidSudoku(board2))  # False