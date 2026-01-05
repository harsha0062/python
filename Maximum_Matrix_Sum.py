# Import typing for type hints
from typing import List

# Function to compute the maximum matrix sum
# by flipping signs of elements optimally
# NOTE: The logic and body of this function are exactly as provided.

def maxMatrixSum(matrix: List[List[int]]) -> int:
    total = 0                 # To store sum of absolute values of all elements
    min_abs_val = float("inf")  # To track the smallest absolute value in the matrix
    negative_count = 0        # To count how many negative numbers are in the matrix

    # Traverse each row in the matrix
    for row in matrix:
        # Traverse each value in the current row
        for val in row:
            # Add absolute value of current element to total
            total += abs(val)

            # Count negative values
            if val < 0:
                negative_count += 1

            # Track the minimum absolute value in the entire matrix
            min_abs_val = min(min_abs_val, abs(val))

    # If the count of negative numbers is odd,
    # one element must remain negative after optimal flips.
    # Subtract twice the smallest absolute value to adjust total.
    if negative_count % 2 != 0:
        total -= 2 * min_abs_val

    # Return the maximum possible matrix sum
    return total


# ------------- Input and Output Section -------------

# Example input matrix
matrix = [
    [1, -1, -1],
    [-1, -1, -1],
    [1, 1, 1]
]

# Call the function with the example matrix
result = maxMatrixSum(matrix)

# Print input and output
print("Input matrix:")
for row in matrix:
    print(row)

print("Maximum matrix sum:", result)
