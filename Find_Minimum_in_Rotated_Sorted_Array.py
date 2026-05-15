def findMin(nums: list[int]) -> int:
    """
    Find minimum element in rotated sorted array using binary search.
    After rotation k times, array has form [k+1, ..., n, 1, 2, ..., k].
    Binary search: compare mid with right to decide which half contains minimum.
    """
    l = 0
    r = len(nums) - 1
    
    while l < r:
        # Fix mid calculation: (l + (r-l)//2) == (l+r)//2
        mid = l + (r - l) // 2
        
        # If mid > right, minimum in right half (including mid+1)
        if nums[mid] > nums[r]:
            l = mid + 1
        # mid <= right, minimum in left half (including mid)
        else:
            r = mid
    
    return nums[l]  # Minimum found


# Test cases with inputs inside code
print("nums=[3,4,5,1,2] ->", findMin([3,4,5,1,2]))    # 1 (rotated 3,4,5,1,2)
print("nums=[4,5,6,7,0,1,2] ->", findMin([4,5,6,7,0,1,2]))  # 0
print("nums=[11,13,15,17] ->", findMin([11,13,15,17]))  # 11 (no rotation)
print("nums=[1] ->", findMin([1]))                      # 1

# Visualize binary search:
print("\nBinary search for [3,4,5,1,2]:")
nums = [3,4,5,1,2]; l, r = 0, 4
print("l=0,r=4")
while l < r:
    mid = l + (r-l)//2
    print(f"mid={mid}({nums[mid]}), nums[mid]={nums[mid]} > nums[r]={nums[r]}? {'Yes' if nums[mid]>nums[r] else 'No'}")
    if nums[mid] > nums[r]:
        l = mid + 1
        print("  l=mid+1 →", l)
    else:
        r = mid
        print("  r=mid  →", r)
print(f"Min={nums[l]}")