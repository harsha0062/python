from typing import List

def minRemoval(nums: List[int], k: int) -> int:
    """
    Find the minimum number of elements to remove so that every element 
    nums[i] satisfies nums[i] * k >= nums[j] for all j <= i.
    
    Args:
        nums: List of integers
        k: Positive integer multiplier constraint
    
    Returns:
        Minimum removals needed
    """
    n = len(nums)
    nums.sort()  # Sort array to use sliding window on sorted order
    mx = 0       # Track maximum valid window size

    l = 0        # Left pointer of sliding window
    for r in range(n):  # Right pointer expands window
        # Shrink window while nums[l] * k < nums[r] (condition violated)
        while l < r and nums[l] * k < nums[r]:
            l += 1
        # Update maximum valid window size
        mx = max(mx, r - l + 1)
    
    return n - mx  # Minimum removals = total length - max valid window

# Test input inside the code
nums = [5, 10, 3, 10, 15]  # Example input
k = 2                       # Example k value

# Calculate and print result
result = minRemoval(nums, k)
print(f"Input: nums = {nums}, k = {k}")
print(f"Minimum removals needed: {result}")
print(f"Largest valid subarray length: {len(nums) - result}")
