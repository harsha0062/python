from typing import List

class Solution:
    def countBattleships(self, grid: List[List[str]]) -> int:
        """
        Count the number of battleships in the board.

        Idea:
        - Each battleship is a connected component of 'X' cells.
        - Use DFS to visit all connected 'X' cells.
        - Every time we find an unvisited 'X', that means a new battleship.
        """
        n, m = len(grid), len(grid[0])

        # Keep track of visited cells so we do not count the same ship twice
        visited = set()

        def dfs(i, j):
            # Stop if out of bounds, already visited, or current cell is not part of a ship
            if i < 0 or i >= n or j < 0 or j >= m or (i, j) in visited or grid[i][j] != "X":
                return

            # Mark the current ship cell as visited
            visited.add((i, j))

            # Explore all 4 directions
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        count = 0

        # Traverse every cell in the board
        for i in range(n):
            for j in range(m):
                # If we find an unvisited ship cell, it starts a new battleship
                if grid[i][j] == "X" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1

        return count


# Input inside the code
sol = Solution()

grid1 = [
    ["X", ".", ".", "X"],
    [".", ".", ".", "X"],
    [".", ".", ".", "X"]
]
print(sol.countBattleships(grid1))

grid2 = [
    ["X", "X", "X"],
    [".", ".", "."],
    ["X", ".", "X"]
]
print(sol.countBattleships(grid2))

grid3 = [
    [".", "."],
    [".", "."]
]
print(sol.countBattleships(grid3))