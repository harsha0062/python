from typing import List

def findMin(nums: List[int]) -> int:
    """
    Two methods to find minimum in (rotated) sorted array.

    Method 1: Binary search (O(log n)) – works on rotated sorted array.
    Method 2: Sorting (O(n log n)) – always works but less efficient.

    You can switch between methods by uncommenting one and commenting the other.
    """
    # ===== Method 1: Binary search (for rotated sorted array) =====
    l = 0
    h = len(nums) - 1

    while l < h:
        mid = l + (h - l) // 2

        if nums[mid] > nums[h]:
            # Minimum is in the right half
            l = mid + 1
        elif nums[mid] > nums[l]:
            # Minimum is in the left half (but not necessarily mid)
            h = mid
        else:
            # nums[mid] <= nums[l] and possibly equal to nums[h]
            h -= 1

    return nums[h]


# ===== Method 2: Simply sort and return first element =====
def findMin_sort(nums: List[int]) -> int:
    nums_sorted = sorted(nums)  # Do not mutate original if needed
    return nums_sorted[0]


# Test cases with inputs inside code (no if __name__ == "__main__")
nums1 = [3, 4, 5, 1, 2]
nums2 = [4, 5, 6, 7, 0, 1, 2]
nums3 = [11, 13, 15, 17]

print("nums1 =", nums1)
print("Method 1 (binary search) ->", findMin(nums1.copy()))      # 1
print("Method 2 (sort + nums[0]) ->", findMin_sort(nums1.copy())) # 1

print("nums2 =", nums2)
print("Method 1 (binary search) ->", findMin(nums2.copy()))      # 0
print("Method 2 (sort + nums[0]) ->", findMin_sort(nums2.copy())) # 0

print("nums3 =", nums3)
print("Method 1 (binary search) ->", findMin(nums3.copy()))      # 11
print("Method 2 (sort + nums[0]) ->", findMin_sort(nums3.copy())) # 11