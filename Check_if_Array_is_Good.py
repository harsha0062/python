def isGood(nums: list[int]) -> bool:
    """
    Check if nums forms a "good" array: contains {1,2,...,n-1,n,n} exactly once each.
    Sorted array must be exactly [1,2,3,...,n-1,n,n] where n = len(nums).
    """
    n = len(nums)
    nums.sort()              # Sort to check consecutive order
    
    expected = 1             # Expected value starts at 1
    for i in range(n):
        if nums[i] != expected:
            return False     # Missing or duplicate found
        
        # For all but last 2 elements, expect next consecutive number
        if i < n - 2:
            expected += 1
    
    # Final check: array length must be n+1 where n=nums[-1]
    return n == nums[-1] + 1


# Test cases with inputs inside code
print("nums=[2,1,3] ->", isGood([2,1,3]))      # True: sorted=[1,2,3], n=3, 3==3 ✓
print("nums=[1,2,3,4] ->", isGood([1,2,3,4]))  # False: sorted=[1,2,3,4], n=4, 4!=5 ✗
print("nums=[1,1] ->", isGood([1,1]))          # True: sorted=[1,1], n=2, 2==1+1 ✓
print("nums=[3,4,4,1,2,1] ->", isGood([3,4,4,1,2,1]))  # True

# Visualize validation logic:
print("\nValidation for [2,1,3]:")
nums = sorted([2,1,3])
n = len(nums)
print(f"Sorted: {nums}")
print(f"Expected sequence: 1→2→3 (then check n=3 == nums[-1]=3)")

expected = 1
for i in range(n):
    print(f"i={i}: nums[{i}]={nums[i]} == expected={expected} → {'✓' if nums[i]==expected else '✗'}")
    if nums[i] != expected:
        print("  FAIL")
        break
    if i < n-2:
        expected += 1
print(f"Final check: len={n} == nums[-1]+1={nums[-1]+1} → {'✓' if n==nums[-1]+1 else '✗'}")