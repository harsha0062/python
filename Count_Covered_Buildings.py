from typing import List

# Function to count how many buildings are "covered"
# A building [x, y] is covered if there is at least one building:
#   - to its left  (same row y, smaller column x)
#   - to its right (same row y, larger column x)
#   - above it     (same column x, smaller row y)
#   - below it     (same column x, larger row y)
def countCoveredBuildings(n: int, buildings: List[List[int]]) -> int:
    # For each row index y, track:
    #   max_row[y] = maximum x (rightmost building in that row)
    #   min_row[y] = minimum x (leftmost building in that row)
    max_row = [0] * (n + 1)
    min_row = [n + 1] * (n + 1)

    # For each column index x, track:
    #   max_col[x] = maximum y (bottom-most building in that column)
    #   min_col[x] = minimum y (top-most building in that column)
    max_col = [0] * (n + 1)
    min_col = [n + 1] * (n + 1)

    # First pass: compute min/max for each row and column
    for p in buildings:
        x, y = p[0], p[1]
        # Update row boundaries for this y (row)
        max_row[y] = max(max_row[y], x)
        min_row[y] = min(min_row[y], x)
        # Update column boundaries for this x (column)
        max_col[x] = max(max_col[x], y)
        min_col[x] = min(min_col[x], y)

    # Second pass: count how many buildings are strictly between
    # the extremes in both its row and its column
    res = 0
    for x, y in buildings:
        # x is between min_row[y] and max_row[y]  -> has left and right neighbor
        # y is between min_col[x] and max_col[x]  -> has above and below neighbor
        if x > min_row[y] and x < max_row[y] and y > min_col[x] and y < max_col[x]:
            res += 1

    return res


# Example input
n = 3
buildings = [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]

# Call the function and print the result
answer = countCoveredBuildings(n, buildings)
print(answer)  # Expected output: 1 for this example
