def islandPerimeter(grid: list[list[int]]) -> int:
    """
    Calculate island perimeter using DFS: count exposed edges (adjacent water or boundary).
    Each land cell contributes 1 edge for each side that is water or boundary.

    Assumptions:
        - Exactly one island (one connected component).
        - No lakes (water is entirely outside the island).
        - Start DFS from any land cell; it will visit all island cells.
    """
    visit = set()
    rows, cols = len(grid), len(grid[0])

    def dfs(i: int, j: int) -> int:
        # Case 1: out of grid or water → this side is an exposed edge (counts as +1)
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
            return 1

        # Case 2: already visited → no additional edge
        if (i, j) in visit:
            return 0

        # Mark this land cell as visited
        visit.add((i, j))

        # Recursively get perimeter contribution from all four directions
        perimeter = 0
        perimeter += dfs(i + 1, j)  # down
        perimeter += dfs(i - 1, j)  # up
        perimeter += dfs(i, j + 1)  # right
        perimeter += dfs(i, j - 1)  # left

        return perimeter

    # Start from any land cell (only one island)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                return dfs(i, j)

    # No land found → perimeter = 0
    return 0


# Test cases with inputs inside code (no `if __name__ == "__main__"`)
grid1 = [[0, 1, 0, 0],
         [1, 1, 1, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 0]]
print("grid1 perimeter =", islandPerimeter(grid1))  # Expected: 12

grid2 = [[1]]  # 1x1 land cell, 4 edges exposed
print("grid2 perimeter =", islandPerimeter(grid2))  # Expected: 4

grid3 = [[1, 0]]  # 1x2, only left and top/bottom sides exposed
print("grid3 perimeter =", islandPerimeter(grid3))  # Expected: 4

# Trace the DFS for grid1:
print("\nGrid1 (12 perimeter) for visual check:")
print("row 0:", grid1[0])
print("row 1:", grid1[1])
print("row 2:", grid1[2])
print("row 3:", grid1[3])