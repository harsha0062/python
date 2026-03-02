from typing import List

def minSwaps(grid: List[List[int]]) -> int:
    n = len(grid)
    
    # Helper: count trailing zeros from right in a single row
    def tzeros(row):
        c = 0
        # traverse from last element to first
        for i in range(n - 1, -1, -1):
            if row[i] != 0:
                break
            c += 1
        return c

    # Build array of trailing zeros for each row
    arr = [tzeros(row) for row in grid]

    res = 0
    # For each row i, the required trailing zeros is n - i - 1
    for i in range(n):
        target = n - i - 1
        if arr[i] >= target:
            continue  # already satisfies the condition; no swap needed

        # Otherwise, look for the first row j (j > i) that has at least `target` zeros
        found = False
        for j in range(i + 1, n):
            if arr[j] >= target:
                # We need to swap row j up to position i by adjacent swaps
                # The number of swaps is (j - i)
                res += j - i
                
                # Simulate swapping row j up to position i:
                # Shift elements from i to j-1 one position right, then put arr[j] at i
                # (We are only updating the `arr` array, not the actual grid.)
                for k in range(j, i, -1):
                    arr[k] = arr[k - 1]
                found = True
                break

        # If no suitable row is found, arrangement is impossible
        if not found:
            return -1

    return res


# Example input (you can change this)
grid = [
    [0, 0, 1],
    [1, 1, 0],
    [1, 0, 0]
]

# Run the function
print(minSwaps(grid))
