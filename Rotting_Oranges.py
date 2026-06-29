from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Return the minimum number of minutes needed for all fresh oranges to rot.

        Idea:
        - Put all initially rotten oranges into a queue.
        - Count how many fresh oranges exist.
        - Run multi-source BFS level by level.
        - Each BFS level represents 1 minute.
        - Whenever a fresh orange becomes rotten, push it into the queue.
        - If fresh oranges remain at the end, return -1.
        """
        n, m = len(grid), len(grid[0])

        # Queue holds all rotten oranges that can spread rot
        q = deque()

        # Count fresh oranges
        fresh_org = 0

        # Collect starting rotten oranges and count fresh ones
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_org += 1

        # If there are no fresh oranges, answer is 0 minutes
        if fresh_org == 0:
            return 0

        # Directions: right, down, up, left
        dic = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # Keep track of cells already visited/rotted during BFS
        visited = set(q)

        # Minutes elapsed
        count = 0

        # BFS level by level
        while q and fresh_org > 0:
            count += 1

            # Process all rotten oranges present at this minute
            for _ in range(len(q)):
                row, col = q.popleft()

                # Try to rot 4-directionally adjacent oranges
                for rw, cl in dic:
                    new_row = row + rw
                    new_col = col + cl

                    if (
                        0 <= new_row < n
                        and 0 <= new_col < m
                        and grid[new_row][new_col] == 1
                        and (new_row, new_col) not in visited
                    ):
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))
                        fresh_org -= 1

        # If all fresh oranges are rotten, return time taken; otherwise impossible
        return count if fresh_org == 0 else -1


# Input inside the code
sol = Solution()

grid1 = [[2,1,1],[1,1,0],[0,1,1]]
print(sol.orangesRotting(grid1))

grid2 = [[2,1,1],[0,1,1],[1,0,1]]
print(sol.orangesRotting(grid2))

grid3 = [[0,2]]
print(sol.orangesRotting(grid3))