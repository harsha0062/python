from typing import List
from math import inf

def maxTotalValue(nums: List[int], k: int) -> int:
    """
    Compute the maximum total value based on the range (max - min) of the array, multiplied by k.

    Logic:
        - Find the maximum element (mx) and minimum element (mn) in nums.
        - Return (mx - mn) * k.

    This matches the given implementation exactly.
    """
    mx = -inf
    mn = inf

    for n in nums:
        if n > mx:
            mx = n
        if n < mn:
            mn = n

    return (mx - mn) * k


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
nums1 = [1, 3, 2, 5, 4]
k1 = 2
print("nums1 =", nums1)
print("k1 =", k1)
print("maxTotalValue =", maxTotalValue(nums1, k1))
# mx = 5, mn = 1 → (5 - 1) * 2 = 8

nums2 = [-5, -2, 0, 3, 10]
k2 = 3
print("\nnums2 =", nums2)
print("k2 =", k2)
print("maxTotalValue =", maxTotalValue(nums2, k2))
# mx = 10, mn = -5 → (10 - (-5)) * 3 = 15 * 3 = 45

nums3 = [7, 7, 7, 7]
k3 = 5
print("\nnums3 =", nums3)
print("k3 =", k3)
print("maxTotalValue =", maxTotalValue(nums3, k3))
# mx = 7, mn = 7 → (7 - 7) * 5 = 0