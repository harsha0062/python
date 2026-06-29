from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Count the number of islands in a 2D grid.

        Idea:
        - An island is a connected group of '1's.
        - Use DFS to visit all cells in the same island.
        - Every time we find an unvisited '1', that starts a new island.
        """
        n, m = len(grid), len(grid[0])

        # Store visited land cells
        visited = set()

        def dfs(i, j):
            # Stop if out of bounds, already visited, or water
            if i < 0 or i >= n or j < 0 or j >= m or (i, j) in visited or grid[i][j] == "0":
                return

            # Mark this land cell as visited
            visited.add((i, j))

            # Explore all 4 directions
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        count = 0

        # Traverse every cell in the grid
        for i in range(n):
            for j in range(m):
                # If this is unvisited land, it is a new island
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1

        return count


# Input inside the code
sol = Solution()

grid1 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(sol.numIslands(grid1))

grid2 = [
    ["1", "1", "1"],
    ["0", "1", "0"],
    ["1", "1", "1"]
]
print(sol.numIslands(grid2))

grid3 = [
    ["0", "0"],
    ["0", "0"]
]
print(sol.numIslands(grid3))