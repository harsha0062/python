def maxAreaOfIsland(grid: list[list[int]]) -> int:
    """
    Find maximum area of any island (connected 1‑cell group) in 4 directions.
    Uses DFS per land cell to compute island size, global max over all islands.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visit = set()
    maxi = 0

    def dfs(i: int, j: int) -> int:
        # Out of bounds, water, or already visited → no area
        if (i < 0
            or i >= rows
            or j < 0
            or j >= cols
            or grid[i][j] == 0
            or (i, j) in visit):
            return 0

        visit.add((i, j))  # Mark as visited

        # Area = 1 (this cell) plus recursive areas from 4‑direction neighbors
        area = 1
        area += dfs(i + 1, j)   # down
        area += dfs(i - 1, j)   # up
        area += dfs(i, j + 1)   # right
        area += dfs(i, j - 1)   # left
        return area

    # Check every cell; if it's land, start DFS from it
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                maxi = max(maxi, dfs(i, j))

    return maxi


# Test cases with inputs inside code (no `if __name__ == "__main__"`)
grid1 = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print("grid1 max area =", maxAreaOfIsland(grid1.copy()))  # Expected: 6

grid2 = [[0, 0, 0, 0, 0, 0, 0, 0]]
print("grid2 max area =", maxAreaOfIsland(grid2.copy()))  # 0

grid3 = [[1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1],
         [0, 0, 0, 1, 1]]
print("grid3 max area =", maxAreaOfIsland(grid3.copy()))  # 4

# Trace DFS for a small island:
grid4 = [[1, 1],
         [1, 0]]
print("grid4 trace:")
print("DFS from (0,0): explores (0,0)→(0,1)→(1,0) → area 3")