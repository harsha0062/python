from typing import List

# No class solution, and the function name/signature is kept the same.
def zigZagArrays(n: int, l: int, r: int) -> int:
    MOD = 10**9 + 7

    # We shift values from [l, r] to [0, r-l]
    r -= l

    # dp[i][j] = number of valid arrays of length i+1 ending with value j
    dp = [[0] * (r + 1) for _ in range(n)]

    # Base case:
    # For length 1, any value in the range can be chosen once.
    for j in range(r + 1):
        dp[0][j] = 1

    # Build the DP row by row
    for i in range(1, n):
        prev = 0

        if i % 2 == 1:
            # Odd index:
            # current value must be greater than previous value
            # So for each j, count all ways ending with a smaller value.
            for j in range(r + 1):
                dp[i][j] = prev
                prev = (prev + dp[i - 1][j]) % MOD
        else:
            # Even index:
            # current value must be smaller than previous value
            # So for each j, count all ways ending with a larger value.
            for j in range(r, -1, -1):
                dp[i][j] = prev
                prev = (prev + dp[i - 1][j]) % MOD

    # Final answer:
    # Sum all valid endings in the last row.
    return sum(dp[-1]) % MOD


# -------------------
# Input inside code
# -------------------

# Example 1
n = 3
l = 1
r = 3
print(zigZagArrays(n, l, r))

# Example 2
n = 4
l = 2
r = 5
print(zigZagArrays(n, l, r))

# Example 3
n = 1
l = 10
r = 12
print(zigZagArrays(n, l, r))