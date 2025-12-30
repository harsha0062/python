from typing import List

# Function to count number of 3x3 magic squares in the grid
def numMagicSquaresInside(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    res = 0

    # Helper function to check if a 3x3 grid starting at (r, c) is magic
    def isMagic3x3(r: int, c: int) -> bool:
        # Array to track numbers 1 to 9 (index 1–9 used)
        seen = [0] * 16  

        # 1️⃣ Check all numbers are unique and between 1 and 9
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                v = grid[i][j]
                if v < 1 or v > 9 or seen[v]:
                    return False
                seen[v] = 1

        # 2️⃣ Check row sums
        s1 = grid[r][c] + grid[r][c + 1] + grid[r][c + 2]
        s2 = grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2]
        s3 = grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2]
        if not (s1 == s2 == s3):
            return False

        # 3️⃣ Check column sums
        c1 = grid[r][c] + grid[r + 1][c] + grid[r + 2][c]
        c2 = grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1]
        c3 = grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2]
        if not (c1 == c2 == c3 == s1):
            return False

        # 4️⃣ Check diagonal sums
        d1 = grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2]
        d2 = grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c]
        return d1 == d2 == s1

    # Check every possible 3x3 subgrid
    for r in range(rows - 2):
        for c in range(cols - 2):
            if isMagic3x3(r, c):
                res += 1

    return res


# 🔹 INPUT GIVEN DIRECTLY INSIDE THE CODE
grid = [
    [4, 3, 8, 4],
    [9, 5, 1, 9],
    [2, 7, 6, 2]
]

# Function call
result = numMagicSquaresInside(grid)

# Output
print("Number of magic 3x3 squares:", result)
