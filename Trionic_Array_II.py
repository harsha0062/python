from typing import List
from math import inf

def maxSumTrionic(nums: List[int]) -> int:
    """
    Finds the maximum sum of a trionic pattern in the array:
    - Increasing sequence (valley start)
    - Decreasing sequence (peak)
    - Another increasing sequence (valley end)
    Returns -inf if no valid trionic pattern exists.
    """
    n = len(nums)
    res = -inf  # Track maximum sum found
    
    i = 0
    while i < n: 
        # Find end of first increasing sequence (valley to peak start)
        j = i + 1
        while j < n and nums[j] > nums[j-1]:
            j += 1
        p = j - 1  # Peak index (end of first increasing sequence)

        # Skip if no increasing sequence found (single element)
        if p == i:
            i += 1
            continue
            
        # Start with peak and previous element
        curr = nums[p] + nums[p-1]
        
        # Find end of decreasing sequence from peak
        while j < n and nums[j] < nums[j-1]:
            curr += nums[j]
            j += 1
        q = j - 1  # End of decreasing sequence (second valley)

        # Skip invalid patterns:
        # - No decreasing sequence (p == q)
        # - Pattern ends at array end (q == n-1) 
        # - Next element equals current (nums[q] == nums[j])
        if p == q or q == n-1 or (q < n-1 and nums[q] == nums[j]):
            i = q
            continue
        
        # Add the element after second valley (start of second increasing sequence)
        curr += nums[j]
        j += 1

        # Find maximum prefix sum of second increasing sequence
        acc = 0
        mx = 0
        while j < n and nums[j] > nums[j-1]:
            acc += nums[j]
            mx = max(mx, acc)  # Track max prefix sum
            j += 1
        curr += mx  # Add max prefix sum to total

        # Find maximum prefix sum of first decreasing sequence (left side)
        acc = 0
        mx = 0
        jj = p - 2  # Start from element before peak's previous
        while jj >= 0 and nums[jj] < nums[jj+1]:
            acc += nums[jj]
            mx = max(mx, acc)  # Track max prefix sum from left
            jj -= 1
        curr += mx  # Add max left prefix sum to total

        # Update result with current trionic sum
        res = max(res, curr)
        i = q  # Move to end of current pattern
    
    return res

# Test input inside the code
nums = [5, 2, 8, 3, 1, 7, 4, 9, 6]
print(f"Input: {nums}")
result = maxSumTrionic(nums)
print(f"Maximum Trionic Sum: {result}")
