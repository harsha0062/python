def getMinDistance(nums: list[int], target: int, start: int) -> int:
    """
    Find minimum distance from start index to any index containing target value.
    Single pass: track minimum |i - start| for all i where nums[i] == target.
    """
    n = len(nums)
    b = n                       # Initialize to max possible distance (n-1 < n)
    
    for i in range(n):
        if nums[i] == target:   # Found target
            b = min(b, abs(i - start))  # Update minimum distance
    
    return b


# Test cases with inputs inside code
nums1 = [1,2,3,2,2]
target1, start1 = 2, 2
print(f"nums={nums1}, target={target1}, start={start1} ->", 
      getMinDistance(nums1, target1, start1))  # Expected: 0 (already at target)

nums2 = [1,2,3,2,2]
target2, start2 = 2, 3
print(f"nums={nums2}, target={target2}, start={start2} ->", 
      getMinDistance(nums2, target2, start2))  # Expected: 1

nums3 = [1,2,3,4,5]
target3, start3 = 5, 3
print(f"nums={nums3}, target={target3}, start={start3} ->", 
      getMinDistance(nums3, target3, start3))  # Expected: 2

# Visualize distances:
print("\nDistances for nums2=[1,2,3,2,2], target=2, start=3:")
nums = [1,2,3,2,2]; target = 2; start = 3
print("Index:  0  1  2  3  4")
print(f"Value:  {nums[0]} {nums[1]} {nums[2]} {nums[3]} {nums[4]}")
print("Target? N  Y  N  Y  Y")
distances = [abs(i-start) if nums[i]==target else '-' for i in range(len(nums))]
print(f"Dist:   {' '.join([str(d) if isinstance(d,int) else d for d in distances])}")
print(f"Minimum: {min([d for d in distances if isinstance(d,int)])}")