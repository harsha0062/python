from typing import List

def generate(numRows: int) -> List[List[int]]:
    """
    Generates Pascal's triangle with numRows rows.
    
    Pascal's triangle is a triangular array where each number is the sum of the two numbers directly above it.
    The outer edges are always 1s.
    
    Args:
        numRows: Number of rows to generate (0 <= numRows <= 30)
    
    Returns:
        List of lists representing Pascal's triangle
    """
    # Handle empty case - return empty list
    if numRows == 0:
        return []
    
    # Initialize with first row [1]
    ans = [[1]]
    
    # If only 1 row needed, return immediately
    if numRows == 1:
        return ans
    
    # Generate remaining rows
    for i in range(1, numRows):
        # Get previous row
        prev = ans[i-1]
        # Start new row with 1
        row = [1]
        
        # Calculate middle elements: each is sum of two elements from previous row
        for j in range(0, i-1):  # i-1 elements in middle for row i
            row.append(prev[j] + prev[j+1])
        
        # End row with 1
        row.append(1)
        # Add completed row to result
        ans.append(row)
    
    return ans

# Input example: Generate Pascal's triangle with 5 rows
result = generate(5)

# Print the result
print("Pascal's Triangle (5 rows):")
for i, row in enumerate(result):
    print(f"Row {i}: {row}")

# Expected output:
# Row 0: [1]
# Row 1: [1, 1]
# Row 2: [1, 2, 1]
# Row 3: [1, 3, 3, 1]
# Row 4: [1, 4, 6, 4, 1]
