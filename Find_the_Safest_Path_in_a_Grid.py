from typing import List
from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """
        Find the maximum safeness factor from (0,0) to (n-1,n-1).

        Idea:
        1. Multi-source BFS from all thief cells to compute the distance
           of every cell from its nearest thief.
        2. Use a max-heap to always expand the path with the current highest
           possible safeness factor.
        3. The safeness of a path is the minimum distance along that path.
        """
        n = len(grid)

        def precompute():
            # Multi-source BFS starting from all thief cells (grid[r][c] == 1)
            q = deque()
            min_dist = {}

            for r in range(n):
                for c in range(n):
                    if grid[r][c]:
                        q.append([r, c, 0])
                        min_dist[(r, c)] = 0

            # If there are no thieves, every cell is infinitely safe in principle.
            # But the problem guarantees a meaningful path; this BFS will just
            # leave non-thief cells unfilled otherwise.
            while q:
                r, c, dist = q.popleft()
                nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

                for r2, c2 in nei:
                    if 0 <= r2 < n and 0 <= c2 < n and (r2, c2) not in min_dist:
                        min_dist[(r2, c2)] = dist + 1
                        q.append([r2, c2, dist + 1])

            return min_dist

        # Compute nearest-thief distance for every cell
        min_dist = precompute()

        # Max-heap stores (-current_safeness, row, col)
        maxHeap = [(-min_dist[(0, 0)], 0, 0)]
        visit = set()
        visit.add((0, 0))

        # Best-first search: always take the path with the largest current safeness
        while maxHeap:
            dist, r, c = heapq.heappop(maxHeap)
            dist = -dist

            if (r, c) == (n - 1, n - 1):
                return dist

            nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for r2, c2 in nei:
                if 0 <= r2 < n and 0 <= c2 < n and (r2, c2) not in visit:
                    visit.add((r2, c2))
                    # Path safeness becomes the min of current path safeness and cell safety
                    dist2 = min(dist, min_dist[(r2, c2)])
                    heapq.heappush(maxHeap, (-dist2, r2, c2))


# Input inside the code
sol = Solution()

grid1 = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]
print(sol.maximumSafenessFactor(grid1))

grid2 = [
    [0, 0, 1],
    [0, 0, 0],
    [0, 0, 0]
]
print(sol.maximumSafenessFactor(grid2))

grid3 = [
    [0, 0],
    [0, 0]
]
print(sol.maximumSafenessFactor(grid3))