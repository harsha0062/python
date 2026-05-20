from typing import List

def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    """
    Find two distinct integer lists:
        - answer[0] = all distinct integers in nums1 but not in nums2.
        - answer[1] = all distinct integers in nums2 but not in nums1.

    Uses set operations to avoid duplicates and to check membership in O(1) on average.
    """
    set1 = set(nums1)   # distinct elements in nums1
    set2 = set(nums2)   # distinct elements in nums2
    ans1 = set()        # elements in nums1 ∖ nums2
    ans2 = set()        # elements in nums2 ∖ nums1

    # Find elements in nums1 not in nums2
    for i in nums1:
        if i not in set2:
            ans1.add(i)

    # Find elements in nums2 not in nums1
    for i in nums2:
        if i not in set1:
            ans2.add(i)

    return [list(ans1), list(ans2)]


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
nums1_1 = [1, 2, 3]
nums2_1 = [2, 4, 6]
print("nums1 =", nums1_1)
print("nums2 =", nums2_1)
print("findDifference =", findDifference(nums1_1, nums2_1))
# Expected: [[1, 3], [4, 6]] (order within each list may vary)

nums1_2 = [1, 2, 3, 3]
nums2_2 = [1, 1, 2, 2]
print("nums1 =", nums1_2)
print("nums2 =", nums2_2)
print("findDifference =", findDifference(nums1_2, nums2_2))
# Expected: [[3], []] (distinct elements only)

nums1_3 = [1, 2, 3]
nums2_3 = [4, 5, 6]
print("nums1 =", nums1_3)
print("nums2 =", nums2_3)
print("findDifference =", findDifference(nums1_3, nums2_3))
# Expected: [[1, 2, 3], [4, 5, 6]]

# Simplified variant using set difference (equivalent logic):
print("\nSimplified version (same behavior):")
def findDifference_short(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    s1, s2 = set(nums1), set(nums2)
    return [list(s1 - s2), list(s2 - s1)]

print("Short version:", findDifference_short([1,2,3],[2,4,6]))