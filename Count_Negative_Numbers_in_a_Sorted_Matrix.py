from typing import List  # Import List so the type hint works

# Your function (not changed)
def countNegatives(grid: List[List[int]]) -> int:
    # Initialize counter to 0
    c = 0
    # Iterate over each row in the grid
    for i in grid:
        # Iterate over each element in the current row
        for j in i:
            # Check if current element is negative
            if j < 0:
                # Increment counter if element is negative
                c += 1
    # Return total count of negative numbers
    return c


# Sample input given directly inside the code
# You can change this grid to test with other values
grid = [
    [4, 3, 2, -1],
    [3, 2, 1, -1],
    [1, 1, -1, -2],
    [-1, -1, -2, -3]
]

# Call the function and print the result
result = countNegatives(grid)
print(result)  # Expected output for this grid is 8
