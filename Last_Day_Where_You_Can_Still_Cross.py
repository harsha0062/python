from typing import List
import collections

# DO NOT CHANGE THIS FUNCTION LOGIC
def latestDayToCross(row: int, col: int, cells: List[List[int]]) -> int:
    left, right = 1, len(cells)
    ans = 0

    # This function checks if we can cross the grid on a given day
    def cancross(row, col, cells, day):
        # Create grid (0 = land, 1 = water)
        grid = [[0] * col for _ in range(row)]

        # Mark flooded cells up to 'day'
        for i in range(day):
            r, c = cells[i]
            grid[r - 1][c - 1] = 1

        queue = collections.deque()
        visited = set()

        # Start BFS from all top-row land cells
        for c in range(col):
            if grid[0][c] == 0:
                queue.append((0, c))
                visited.add((0, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # BFS traversal
        while queue:
            r, c = queue.popleft()

            # Reached bottom row → crossing possible
            if r == row - 1:
                return True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < row and
                    0 <= nc < col and
                    grid[nr][nc] == 0 and
                    (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        return False

    # Binary search on days
    while left <= right:
        mid = (left + right) // 2
        if cancross(row, col, cells, mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans


# -------- INPUT GIVEN INSIDE THE CODE --------

row = 2
col = 2
cells = [
    [1, 1],
    [2, 1],
    [1, 2],
    [2, 2]
]

# Call the function
result = latestDayToCross(row, col, cells)

# Output
print("Latest day to cross:", result)
