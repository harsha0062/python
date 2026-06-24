from typing import List

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        # Shift values from [l, r] to [0, r-l]
        items = r - l + 1

        # dp[i][v][0/1] idea is handled through matrix power:
        # We build a transition matrix of size 2*items.
        # First half  -> last move was "up"
        # Second half -> last move was "down"

        size = 2 * items
        mat = [[0] * size for _ in range(size)]

        # Build transitions:
        # For an "up" state ending at value i, next value must be smaller for "down" states,
        # and for a "down" state ending at value i, next value must be larger for "up" states.
        for i in range(items):
            for j in range(i):
                # From lower value j to higher value i => can form an "up" transition
                mat[i][j + items] = 1
            for j in range(i + 1, items):
                # From higher value j to lower value i => can form a "down" transition
                mat[i + items][j] = 1

        # Multiply matrices: A * B
        def mul(a, b):
            n1, m1 = len(a), len(a[0])
            n2, m2 = len(b), len(b[0])
            res = [[0] * m2 for _ in range(n1)]
            for i in range(n1):
                for k in range(m1):
                    if a[i][k] == 0:
                        continue
                    for j in range(m2):
                        if b[k][j]:
                            res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
            return res

        # Fast exponentiation of the transition matrix
        def powMul(base, exp, res):
            while exp:
                if exp % 2 == 1:
                    res = mul(res, base)
                base = mul(base, base)
                exp //= 2
            return res

        # Initial state:
        # For length 1, every value is valid in both state groups.
        dp = [[1] * size]

        # Apply transitions n-1 times to get arrays of length n
        dp = powMul(mat, n - 1, dp)

        # Sum all ending states
        return sum(dp[-1]) % MOD


# -------------------
# Input inside code
# -------------------

sol = Solution()

n1, l1, r1 = 3, 1, 3
print(sol.zigZagArrays(n1, l1, r1))

n2, l2, r2 = 4, 2, 5
print(sol.zigZagArrays(n2, l2, r2))

n3, l3, r3 = 1, 7, 9
print(sol.zigZagArrays(n3, l3, r3))