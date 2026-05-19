def getCommon(nums1: list[int], nums2: list[int]) -> int:
    """
    Find the smallest integer common to both nums1 and nums2.
    Both arrays are sorted in non‑decreasing order.

    Uses two pointers:
        - i for nums1, j for nums2
        - if nums1[i] == nums2[j] → this is the smallest common value (because arrays are sorted), so return it.
        - if nums1[i] < nums2[j] → i++ to try a larger value in nums1.
        - if nums1[i] > nums2[j] → j++ to try a larger value in nums2.

    If no common value is found, return -1.
    """
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            return nums1[i]
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return -1


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
nums1_1 = [1, 2, 3]
nums2_1 = [2, 4]
print("nums1 =", nums1_1)
print("nums2 =", nums2_1)
print("getCommon =", getCommon(nums1_1, nums2_1))  # 2

nums1_2 = [1, 2, 3, 6]
nums2_2 = [2, 3, 4, 5]
print("nums1 =", nums1_2)
print("nums2 =", nums2_2)
print("getCommon =", getCommon(nums1_2, nums2_2))  # 2

nums1_3 = [1, 2, 3]
nums2_3 = [4, 5, 6]
print("nums1 =", nums1_3)
print("nums2 =", nums2_3)
print("getCommon =", getCommon(nums1_3, nums2_3))  # -1