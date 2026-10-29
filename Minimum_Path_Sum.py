
def minPathSum(grid):
    # Get the number of rows and columns
    rows, cols = len(grid), len(grid[0])

    # Create a DP table with an extra row and column.
    # Use infinity as the default value so invalid paths are ignored.
    res = [[float("inf")] * (cols + 1) for _ in range(rows + 1)]

    # Set the virtual bottom-right boundary to 0.
    # This allows the bottom-right cell to calculate correctly.
    res[rows - 1][cols] = 0

    # Traverse the grid from bottom-right to top-left
    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            # Current cell cost plus the minimum cost from either
            # the cell below or the cell to the right
            res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])

    # Return the minimum path sum starting from the top-left cell
    return res[0][0]


# Input inside the code
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

print(minPathSum(grid))
