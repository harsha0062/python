from typing import List

def numSpecial(mat: List[List[int]]) -> int:
    """
    Count special positions in a binary matrix.
    A special position (i,j) has mat[i][j] == 1 and is the only 1 in row i and column j.
    """
    m = len(mat)
    n = len(mat[0])

    def checkcol(mat, i, j):
        # Check if column j has exactly one 1 (only at row i)
        for k in range(len(mat)):
            if(mat[k][j] == 1 and k == i):
                continue
            elif(mat[k][j] == 1):
                return False
        return True
    
    def checkrow(mat, i, j):
        # Check if row i has exactly one 1 (only at column j)
        for k in range(len(mat[0])):
            if(mat[i][k] == 1 and k == j):
                continue
            elif(mat[i][k] == 1):
                return False
        return True
    
    ans = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1 and checkcol(mat, i, j) and checkrow(mat, i, j):
                ans += 1
    return ans  # Fixed typo: was 'ansg'

# Test input from LeetCode example 1
mat = [[1,0,0],[0,0,1],[1,0,0]]
print(numSpecial(mat))  # Expected: 1 (position [0][0])

# Test input from LeetCode example 2  
mat2 = [[1,0,0],[0,1,0],[0,0,1]]
print(numSpecial(mat2))  # Expected: 3 (all diagonal positions)
