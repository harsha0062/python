def maximalRectangle(mat: list[list[str]]) -> int:
    """
    Find largest rectangle of '1's in binary matrix using histogram area technique per row.
    Treat each row as base of histogram (height=consecutive '1's above), compute largest rectangle in histogram.
    Uses monotonic stack to compute largest rectangle area efficiently.
    """
    if not mat or not mat[0]:
        return 0
    
    n = len(mat)              # rows
    m = len(mat[0])           # cols
    
    height = [0] * (m + 1)    # heights[i] = consecutive '1's ending at row i, col i
    res = 0                   # max area found
    
    for i in range(n):
        # Update heights for this row
        for j in range(m):
            if mat[i][j] == '1':
                height[j] += 1   # Extend histogram bar
            else:
                height[j] = 0     # Reset on '0'
        
        # Compute largest rectangle in this histogram using stack
        s = [0]                 # Monotonic increasing stack (indices)
        
        for j in range(1, m + 1):
            # Pop bars taller than current height[j]
            while s and height[s[-1]] >= height[j]:
                h = height[s.pop()]           # Height of popped bar
                w = j - 1 - (s[-1] if s else -1)  # Width: right-left-1
                res = max(res, h * w)         # Update max area
            
            s.append(j)               # Push current index
    
    return res


# Test cases with inputs inside code
mat1 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print("mat1 maximal rectangle =", maximalRectangle(mat1))  # Expected: 6

mat2 = [["0"]]
print("mat2 maximal rectangle =", maximalRectangle(mat2))  # Expected: 0

mat3 = [["1","1","1","0"],["1","1","1","0"],["1","1","1","0"]]
print("mat3 maximal rectangle =", maximalRectangle(mat3))  # Expected: 9 (full 3x3)

# Visualize histogram technique for mat3 row 2:
print("\nHistogram heights after row 2: ", [3,3,3,0])