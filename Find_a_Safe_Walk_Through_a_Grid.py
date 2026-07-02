from typing import List
from collections import deque
from math import inf

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        """
        Return True if we can reach the bottom-right cell with health > 0.

        Idea:
        - Each cell has a cost of grid[r][c] (0 or 1).
        - We want the minimum cost path from (0,0) to (n-1,m-1).
        - Use BFS-style relaxation (0-1 BFS) because edge weights are 0 or 1.
        """
        n, m = len(grid), len(grid[0])

        # dist[i][j] = minimum health cost needed to reach cell (i, j)
        dist = [[inf] * m for _ in range(n)]
        dist[0][0] = grid[0][0]

        q = deque()
        q.append((grid[0][0], 0, 0))

        while q:
            c, i, j = q.popleft()

            # Skip outdated states
            if c != dist[i][j]:
                continue

            # Explore 4 directions
            for ni, nj in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue

                nc = c + grid[ni][nj]

                if nc < dist[ni][nj]:
                    dist[ni][nj] = nc

                    # 0-cost move goes to the front, 1-cost move goes to the back
                    if grid[ni][nj] == 0:
                        q.appendleft((nc, ni, nj))
                    else:
                        q.append((nc, ni, nj))

        # Need strictly positive health after paying the path cost
        return dist[n - 1][m - 1] < health


# Test cases
sol = Solution()

grid1 = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
health1 = 2
print(sol.findSafeWalk(grid1, health1))  # True/False depending on path cost

grid2 = [[1, 1], [1, 1]]
health2 = 3
print(sol.findSafeWalk(grid2, health2))

grid3 = [[0]]
health3 = 1
print(sol.findSafeWalk(grid3, health3))