def areSimilar(mat: list[list[int]], k: int) -> bool:
    """
    Check if matrix remains unchanged after rotating each row k positions right.
    Even rows rotate left k, odd rows rotate right k (but code assumes uniform right shift).
    k %= n optimizes for cyclic nature.
    """
    m, n = len(mat), len(mat[0])
    k = k % n                  # Reduce k to [0,n) since rotations repeat every n
    
    for i in range(m):         # Check each row
        for j in range(n):     # Check each position in row
            # After k right shifts, mat[i][j] should equal mat[i][(j+k)%n]
            if mat[i][j] != mat[i][(j + k) % n]:
                return False
    
    return True                # All positions match after rotation


# Test cases with inputs inside code
mat1 = [[1,2,3],[4,5,6],[7,8,9]]
print("mat1=\n", mat1, "\nk=2 ->", areSimilar(mat1, 2))
# Each row rotates right by 2: [1,2,3]→[2,3,1], but original equals rotated?

mat2 = [[1,2,3],[4,5,6]]
print("mat2=\n", mat2, "\nk=0 ->", areSimilar(mat2, 0))      # True (no rotation)
print("mat2=\n", mat2, "\nk=3 ->", areSimilar(mat2, 3))     # True (full cycle)

mat3 = [[1,0,2],[1,2,0]]
print("mat3=\n", mat3, "\nk=1 ->", areSimilar(mat3, 1))
# Row0: [1,0,2] → [2,1,0] ✓
# Row1: [1,2,0] → [0,1,2] ✓

# Visualize rotation check:
print("\nVisualize mat3 with k=1:")
mat = [[1,0,2],[1,2,0]]
k = 1
for i in range(len(mat)):
    print(f"Row {i}: original=[{mat[i][0]},{mat[i][1]},{mat[i][2]}]")
    print(f"      check: pos0={mat[i][0]}=={mat[i][(0+k)%3]}")
    print(f"            pos1={mat[i][1]}=={mat[i][(1+k)%3]}")
    print(f"            pos2={mat[i][2]}=={mat[i][(2+k)%3]}\n")