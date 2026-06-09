from typing import List

def pivotArray(nums: List[int], pivot: int) -> List[int]:
    """
    Rearrange the array such that:
      - All elements less than pivot appear first,
      - Then all elements equal to pivot,
      - Then all elements greater than pivot.
    
    The relative order of elements within each group is preserved.

    Approach:
      - Use three lists: before (less than pivot), mid (equal to pivot), after (greater than pivot).
      - Iterate through nums and distribute elements into these lists.
      - Return before + mid + after.
    """
    before = []  # elements < pivot
    mid = []     # elements == pivot
    after = []   # elements > pivot

    for n in nums:
        if n < pivot:
            before.append(n)
        elif n > pivot:
            after.append(n)
        else:
            mid.append(n)

    return before + mid + after


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
nums1 = [9, 12, 5, 10, 14, 3, 10]
pivot1 = 10
print("nums1 =", nums1)
print("pivot1 =", pivot1)
print("pivotArray =", pivotArray(nums1, pivot1))
# Expected: [9, 5, 3, 10, 10, 12, 14]

nums2 = [-5, 1, -2, 3, -5, 0, -5]
pivot2 = -5
print("\nnums2 =", nums2)
print("pivot2 =", pivot2)
print("pivotArray =", pivotArray(nums2, pivot2))
# Expected: [-5, -5, -5, 1, -2, 3, 0]

nums3 = [1, 2, 3]
pivot3 = 4
print("\nnums3 =", nums3)
print("pivot3 =", pivot3)
print("pivotArray =", pivotArray(nums3, pivot3))
# Expected: [1, 2, 3] (all less than pivot)

nums4 = [5, 5, 5]
pivot4 = 5
print("\nnums4 =", nums4)
print("pivot4 =", pivot4)
print("pivotArray =", pivotArray(nums4, pivot4))
# Expected: [5, 5, 5] (all equal to pivot)