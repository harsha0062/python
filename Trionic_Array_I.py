from typing import List

def isTrionic(nums: List[int]) -> bool:
    n = len(nums)

    # Find end of first increasing segment
    i = 1
    while i < n and nums[i] > nums[i-1]:
        i += 1
    
    p = i - 1  # Peak of first increasing part
    if p == 0:
        return False
    
    # Find end of decreasing segment
    while i < n and nums[i] < nums[i-1]:
        i += 1
    q = i - 1  # Valley of decreasing part
    if q == p:
        return False

    # Find end of second increasing segment
    while i < n and nums[i] > nums[i-1]:
        i += 1
    if i - 1 == q or i < n:  # Must reach exact end, no leftovers
        return False
    
    return True

# Test input inside the code
nums = [1, 3, 2, 4]  # Example: increases to 3, decreases to 2, increases to 4, ends

# Print result
print(f"Input: {nums}")
print(f"Is trionic: {isTrionic(nums)}")  # Output: True
