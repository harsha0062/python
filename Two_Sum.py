from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Finds two indices in nums that add up to target using Two Pointer technique.
    NOTE: This returns indices AFTER sorting, not original positions (LeetCode expects original indices).
    """
    # Create a copy to preserve original array and track original indices
    nums_with_indices = sorted(enumerate(nums), key=lambda x: x[1])  # Sort by value, keep original index
    
    i = 0  # Left pointer
    j = len(nums) - 1  # Right pointer
    
    while i <= j:
        current_sum = nums_with_indices[i][1] + nums_with_indices[j][1]
        
        if current_sum == target:
            # Return ORIGINAL indices
            return [nums_with_indices[i][0], nums_with_indices[j][0]]
        elif current_sum < target:
            i += 1  # Move left pointer right
        else:
            j -= 1  # Move right pointer left
    
    return []  # No solution found

# Test input data
nums = [2, 7, 11, 15]
target = 9

# Execute and print result
result = twoSum(nums, target)
print(f"Input: nums = {nums}, target = {target}")
print(f"Output indices: {result}")  # Expected: [0, 1] since nums[0]+nums[1] = 2+7 = 9
print(f"Verification: nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")

# Additional test case
nums2 = [3, 2, 4]
target2 = 6
result2 = twoSum(nums2, target2)
print(f"\nTest 2 - Input: nums = {nums2}, target = {target2}")
print(f"Output indices: {result2}")  # Expected: [1, 2] since nums[1]+nums[2] = 2+4 = 6
