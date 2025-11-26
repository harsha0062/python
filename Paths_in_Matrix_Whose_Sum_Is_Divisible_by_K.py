from typing import List

# Your function signature kept exactly the same
def numberOfPaths(grid: List[List[int]], k: int) -> int:
    # Number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])

    # 3D DP cache:
    # cache[r][c][rem] = number of valid paths starting from cell (r, c)
    # when current sum % k == rem
    cache = [[[-1] * k for _ in range(cols)] for _ in range(rows)]

    # Modulo as required by the problem
    mod = 10**9 + 7

    # DFS with memoization
    def dfs(r, c, rem):
        # If we are at the bottom-right cell
        if (r == rows - 1) and (c == cols - 1):
            # Add current cell value and update remainder
            rem = (rem + grid[r][c]) % k
            # Valid path if final remainder is 0
            return 0 if rem else 1

        # Out of bounds -> no path
        if r == rows or c == cols:
            return 0

        # If this state already computed, return cached value
        if cache[r][c][rem] > -1:
            return cache[r][c][rem]

        # Update remainder after including current cell
        new_rem = (rem + grid[r][c]) % k

        # Explore both possible moves: down and right
        down_paths = dfs(r + 1, c, new_rem) % mod
        right_paths = dfs(r, c + 1, new_rem) % mod

        # Store result in cache with modulo
        cache[r][c][rem] = (down_paths + right_paths) % mod
        return cache[r][c][rem]

    # Start DFS from top-left with remainder 0
    return dfs(0, 0, 0)


# ----------------- Input inside the code -----------------

# Example grid and k (you can change these to test other cases)
grid = [
    [5, 2, 4],
    [3, 0, 5],
    [0, 7, 2]
]
k = 3

# Call the function and print the answer
ans = numberOfPaths(grid, k)
print(ans)
