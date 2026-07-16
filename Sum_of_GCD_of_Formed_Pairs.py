from typing import List
from math import gcd

def gcdSum(nums: list[int]) -> int:
    """
    Build prefixGcd where:
    prefixGcd[i] = gcd(nums[i], max(nums[0..i]))

    Then:
    - sort prefixGcd
    - pair smallest with largest
    - sum gcd of each pair
    """
    n = len(nums)

    # prefix maximum and prefix gcd-like values
    mx = [nums[0]] * n
    pgcd = [nums[0]] * n

    # Build prefix maximum and gcd(value, prefix maximum)
    for i in range(1, n):
        mx[i] = max(mx[i - 1], nums[i])
        pgcd[i] = gcd(nums[i], mx[i])

    # Sort the transformed values
    pgcd.sort()

    # Pair smallest with largest and add gcd of each pair
    res = 0
    for i in range(n // 2):
        res += gcd(pgcd[i], pgcd[n - i - 1])

    return res


# Input inside the code
nums = [6, 2, 8, 3, 12]

print(gcdSum(nums))