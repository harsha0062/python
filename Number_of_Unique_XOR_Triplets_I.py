from typing import List

def uniqueXorTriplets(nums: List[int]) -> int:
    """
    Return the smallest power of 2 strictly greater than n
    (or n itself when n <= 2, as in your logic).
    """
    n = len(nums)

    # If there are 0, 1, or 2 elements, return n directly
    if n <= 2:
        return n

    # Start from 1 and keep doubling until it becomes greater than n
    ans = 1
    while ans <= n:
        ans <<= 1

    return ans


# Input inside the code
nums = [1, 2, 3, 4]

print(uniqueXorTriplets(nums))