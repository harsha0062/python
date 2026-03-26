def canPartitionGrid(grid: list[list[int]]) -> bool:
    """
    Determine if grid can be partitioned by one horizontal/vertical cut into two connected parts with equal sum.
    Checks rows and columns (via transpose) in both directions using prefix sums + value tracking for connectivity.
    """
    n = len(grid)
    m = len(grid[0])
    total = sum(grid[i][j] for j in range(m) for i in range(n))  # Total sum
    
    def check(g):
        """
        Check if rows in grid g can be partitioned after row i into two connected parts with equal sum.
        Uses prefix sum + tracks positions of each value to verify connectivity.
        """
        nn = len(g)
        mm = len(g[0])
        
        curr = 0              # Prefix sum of rows 0 to i
        seen = {}             # {value: [(first_row,col), (last_row,col)]}
        
        for i in range(nn-1):  # Try cut after each row except last
            for j in range(mm):
                v = g[i][j]
                curr += v
                if v in seen:
                    seen[v][1] = (i, j)  # Update last position
                else:
                    seen[v] = [(i, j), (i, j)]  # First position
        
            diff = total - curr - curr  # Sum above cut - sum below cut
            if diff == 0:
                return True  # Perfect split
            
            if -diff in seen:  # Found compensating value difference
                fr, fc = seen[-diff][0]  # First row,col of compensating value
                lr, lc = seen[-diff][1]  # Last row,col
                
                # Connectivity checks for small grids:
                if mm > 1 and i + 1 > 1:
                    return True  # Big grid: always connected
                if mm > 1 and i + 1 == 1 and (fc == 0 or lc == mm - 1):
                    return True  # One row: edge-connected
                if mm == 1 and (fr == 0 or lr == i):
                    return True  # One column: top/bottom connected
        
        return False
    
    # Check horizontal cuts: rows forward/backward
    if check(grid) or check(grid[::-1]):
        return True
    
    # Transpose for vertical cuts (columns become rows)
    grid = list(zip(*grid))
    
    # Check vertical cuts: columns forward/backward
    if check(grid) or check(grid[::-1]):
        return True
    
    return False


# Test cases with inputs inside code
grid1 = [[1,1],[1,2]]  # total=5, can't partition evenly
print("grid1=\n", grid1, "\n->", canPartitionGrid(grid1))  # Should handle odd sum case

grid2 = [[1,1,1],[1,1,1]]  # total=6, cut after row0: sum=3 each
print("grid2=\n", grid2, "\n->", canPartitionGrid(grid2))  # True

grid3 = [[2,2,2],[2,2,2]]  # total=12, perfect split
print("grid3=\n", grid3, "\n->", canPartitionGrid(grid3))  # True

grid4 = [[1],[2],[3]]  # Vertical split possible
print("grid4=\n", grid4, "\n->", canPartitionGrid(grid4))  # False (total=6, but check logic)