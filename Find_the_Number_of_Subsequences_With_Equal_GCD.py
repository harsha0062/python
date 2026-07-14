from typing import List
from functools import cache
from math import gcd

def subsequencePairCount(nums: List[int]) -> int:
    """
    Count pairs of non-empty disjoint subsequences (seq1, seq2)
    such that gcd(seq1) == gcd(seq2).
    """
    MOD = 10**9 + 7

    @cache
    def dp(i, gcd1, gcd2):
        # Base case: all elements processed
        if i == len(nums):
            # Count only if both subsequences are non-empty and gcds are equal
            return 1 if gcd1 != 0 and gcd1 == gcd2 else 0

        total = 0

        # Option 1: skip nums[i]
        total = (total + dp(i + 1, gcd1, gcd2)) % MOD

        # Option 2: put nums[i] in first subsequence
        new_gcd1 = nums[i] if gcd1 == 0 else gcd(gcd1, nums[i])
        total = (total + dp(i + 1, new_gcd1, gcd2)) % MOD

        # Option 3: put nums[i] in second subsequence
        new_gcd2 = nums[i] if gcd2 == 0 else gcd(gcd2, nums[i])
        total = (total + dp(i + 1, gcd1, new_gcd2)) % MOD

        return total

    return dp(0, 0, 0)


# Input inside the code
nums = [1, 2, 3]

print(subsequencePairCount(nums))