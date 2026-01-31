from typing import List

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    """
    Finds the maximum number of consecutive 1's in a binary array.
    Resets counter when 0 is encountered, tracks maximum streak found.
    """
    ans = 0      # Current streak of consecutive 1's
    maxi = 0     # Maximum streak found so far
    
    for i in nums:
        if i == 0:
            ans = 0      # Reset current streak when 0 found
        else:
            ans += 1     # Increment current streak for each 1
            maxi = max(maxi, ans)  # Update maximum if current streak is larger
    
    return maxi

# Test input data - binary arrays with 0s and 1s
nums1 = [1,1,0,1,1,1]     # Expected: 3 (three 1's at end)
nums2 = [1,0,1,1,0,1]     # Expected: 2 (two 1's in middle)
nums3 = [1,1,1,1]         # Expected: 4 (all 1's)
nums4 = [0,0,0]           # Expected: 0 (no 1's)

# Test cases with output
print(f"Input: {nums1}")
print(f"Output: {findMaxConsecutiveOnes(nums1)}")  # 3

print(f"\nInput: {nums2}")
print(f"Output: {findMaxConsecutiveOnes(nums2)}")  # 2

print(f"\nInput: {nums3}")
print(f"Output: {findMaxConsecutiveOnes(nums3)}")  # 4

print(f"\nInput: {nums4}")
print(f"Output: {findMaxConsecutiveOnes(nums4)}")  # 0
