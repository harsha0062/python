from typing import List
from math import inf

def firstStableIndex(nums: List[int], k: int) -> int:
    n = len(nums)

    # Check every index to see if it satisfies the stability condition
    for i in range(n):
        # Maximum value in the prefix nums[0..i]
        mx = max(nums[:i + 1])

        # Minimum value in the suffix nums[i..n-1]
        mn = min(nums[i:])

        # If the difference between max prefix and min suffix is within k,
        # this is the first stable index
        if mx - mn <= k:
            return i

    # If no stable index is found, return -1
    return -1


# Input inside the code
nums = [1, 3, 2, 5, 4]
k = 2

print(firstStableIndex(nums, k))