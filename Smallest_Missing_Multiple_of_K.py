from typing import List

def missingMultiple(nums: List[int], k: int) -> int:
    # Convert the list to a set for O(1) average time lookups
    nums = set(nums)

    # Start checking from the first positive multiple of k
    curr = k

    # Keep advancing by k as long as the current multiple exists in nums
    while curr in nums:
        curr += k

    # Return the first multiple of k not present in nums
    return curr


# Input inside the code
nums = [2, 4, 8, 10]
k = 2

print(missingMultiple(nums, k))