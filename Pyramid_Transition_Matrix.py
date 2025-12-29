from typing import List
from collections import defaultdict
import itertools

# Your function is kept exactly the same
def pyramidTransition(bottom: str, allowed: List[str]) -> bool:
    # t maps a pair of characters (e.g., ('A','B')) to a list of possible top characters
    t = defaultdict(list)
    for tri in allowed:
        # tri is a string of length 3, e.g., "ABC"
        # (tri, tri) -> tri
        t[(tri, tri)].append(tri)

    # memo will store results for already processed rows to avoid recomputation
    memo = {}

    def solve(row: str) -> bool:
        # If the row length is 1, we have successfully built the pyramid to the top
        if len(row) == 1:
            return True

        # If we have already computed the result for this row, return it
        if row in memo:
            return memo[row]

        # options[i] will be the list of possible characters for position i of the next row
        options = []

        # Build options for the next row by looking at each adjacent pair in the current row
        for i in range(len(row) - 1):
            key = (row[i], row[i + 1])
            # If this pair has some allowed upper characters, add that list to options
            if key in t:
                options.append(t[key])
            else:
                # If any adjacent pair is not found in t, this row cannot lead to a valid pyramid
                memo[row] = False
                return False

        # Try all possible combinations for the next row using Cartesian product
        for next_row in itertools.product(*options):
            # next_row is a tuple of characters, convert it to string
            if solve("".join(next_row)):  # recursive call on the next row
                memo[row] = True
                return True

        # If none of the combinations lead to a valid pyramid, mark this row as False
        memo[row] = False
        return False

    # Start solving from the bottom row
    return solve(bottom)


# ---------------- Sample input and output ----------------

# Example bottom row and allowed transitions
bottom = "XYZ"  # You can change this to test other cases
allowed = ["XYD", "YZE", "DEA", "FFF"]

# Call the function and print the result
ans = pyramidTransition(bottom, allowed)
print(ans)  # Expected True for this sample case[1]