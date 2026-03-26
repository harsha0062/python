def constructProductMatrix(grid: list[list[int]]) -> list[list[int]]:
    """
    Construct product matrix where ans[i][j] = (product of all grid elements) / grid[i][j] % 12345
    Uses prefix * suffix technique: first compute suffix products backward, then multiply by prefix.
    """
    mod = 12345
    n = len(grid)           # rows
    m = len(grid[0])        # cols
    ans = [[1] * m for _ in range(n)]  # Initialize result matrix
    
    # First pass: BACKWARD - compute suffix products (product of all elements after current)
    suffix = 1
    for i in range(n-1, -1, -1):        # Bottom to top
        for j in range(m-1, -1, -1):    # Right to left
            ans[i][j] = suffix           # Store suffix product
            suffix = (suffix * grid[i][j]) % mod  # Update suffix
    
    # Second pass: FORWARD - multiply by prefix products (product of all elements before current)
    prefix = 1
    for i in range(0, n):               # Top to bottom
        for j in range(0, m):           # Left to right
            ans[i][j] = (prefix * ans[i][j]) % mod  # prefix * suffix = total_product
            prefix = (prefix * grid[i][j]) % mod    # Update prefix
    
    return ans


# Test cases with inputs inside code
grid1 = [[1,2],[3,4]]
print("grid=\n", grid1, "\n->\n", constructProductMatrix(grid1))
# Expected: [[24,12],[8,6]] because total_product=24, ans[i][j]=24/grid[i][j]

grid2 = [[12345],[2],[1]]
print("grid=\n", grid2, "\n->\n", constructProductMatrix(grid2))
# Expected: [[1,0],[0,12344]] (mod 12345 handles large numbers)

grid3 = [[1,3],[2,4],[5,6]]
print("grid=\n", grid3, "\n->\n", constructProductMatrix(grid3))
