from typing import List

def uniqueXorTriplets(nums: List[int]) -> int:
    """
    Count the number of unique values formed by XORing three elements
    using the same logic as your original code.
    """
    n = len(nums)
    seen = set()

    # Store XOR of every pair nums[i] ^ nums[j]
    for i in range(n):
        for j in range(i, n):
            seen.add(nums[i] ^ nums[j])

    res = set()

    # XOR each array element with every pair XOR value
    for i in range(n):
        for v in seen:
            res.add(nums[i] ^ v)

    return len(res)


# Input inside the code
nums = [1, 2, 3]

print(uniqueXorTriplets(nums))