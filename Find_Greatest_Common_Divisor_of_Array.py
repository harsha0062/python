from typing import List
from math import gcd

def findGCD(nums: List[int]) -> int:
    """
    Return the GCD of the maximum and minimum values in the array.
    """
    maxi = max(nums)
    mini = min(nums)
    return gcd(maxi, mini)


# Input inside the code
nums = [2, 5, 6, 9, 10]

print(findGCD(nums))