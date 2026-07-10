from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        For each query [l, r]:
        - Take substring s[l:r+1]
        - Build x by concatenating all non-zero digits in order
        - Let sum_digits be the sum of digits in x
        - Return x * sum_digits mod 1e9+7
        """
        MOD = 10**9 + 7
        res = []

        for l, r in queries:
            x = 0
            sm = 0

            for i in range(l, r + 1):
                d = int(s[i])
                if d != 0:
                    x = (x * 10 + d) % MOD
                    sm += d

            res.append((x * sm) % MOD)

        return res


# Test cases inside the code
sol = Solution()

s1 = "10203"
queries1 = [[0, 4], [1, 3], [2, 4]]
print(sol.sumAndMultiply(s1, queries1))  # [738, 36, 9]

s2 = "1002003"
queries2 = [[0, 6], [1, 5], [2, 4]]
print(sol.sumAndMultiply(s2, queries2))