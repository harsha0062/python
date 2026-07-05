from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        """
        Return [maximum_score, number_of_paths] from 'E' to 'S'.

        Rules:
        - You can move down, right, or diagonally down-right.
        - Cells with 'X' are blocked.
        - Digits add to the score.
        - 'E' and 'S' do not add score.
        """
        MOD = 10**9 + 7
        n = len(board)

        # dp[i][j] = [best_score_from_cell_to_end, number_of_ways]
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        dp[n - 1][n - 1] = [0, 1]  # Start from S with score 0 and one way

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'S' or board[i][j] == 'X':
                    continue

                cell_val = 0 if board[i][j] == 'E' else int(board[i][j])

                best = -1
                ways = 0

                # Check reachable next cells: down, right, diagonal
                for ni, nj in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if ni >= n or nj >= n:
                        continue

                    score, count = dp[ni][nj]
                    if score == -1:
                        continue

                    if score > best:
                        best = score
                        ways = count
                    elif score == best:
                        ways = (ways + count) % MOD

                if best != -1:
                    dp[i][j] = [best + cell_val, ways]

        return dp[0][0] if dp[0][0][0] != -1 else [0, 0]


# Test cases inside the code
sol = Solution()

board1 = ["E23", "2X2", "12S"]
print(sol.pathsWithMaxScore(board1))  # [7, 1]

board2 = ["E12", "1X1", "21S"]
print(sol.pathsWithMaxScore(board2))  # [4, 2]

board3 = ["E11", "XXX", "11S"]
print(sol.pathsWithMaxScore(board3))  # [0, 0]