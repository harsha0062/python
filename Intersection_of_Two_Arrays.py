def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Find the intersection of two arrays, as a list of common elements with at most
    one occurrence per element (set‑like behavior, even though return type is list).

    Steps:
      1. Put all elements of nums1 into a set called `seen`.
      2. For each element in nums2:
           - If it is in `seen`, add it to `res` and remove it from `seen`
             so that the same value cannot be added again.
    """
    seen = set(nums1)
    res = []

    for i in nums2:
        if i in seen:
            res.append(i)
            seen.remove(i)  # remove so it won’t be added again

    return res


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
nums1_1 = [1, 2, 2, 1]
nums2_1 = [2, 2]
print("nums1 =", nums1_1)
print("nums2 =", nums2_1)
print("intersection =", intersection(nums1_1.copy(), nums2_1.copy()))  # [2]

nums1_2 = [4, 9, 5]
nums2_2 = [9, 4, 9, 8, 4]
print("nums1 =", nums1_2)
print("nums2 =", nums2_2)
print("intersection =", intersection(nums1_2.copy(), nums2_2.copy()))  # [9, 4] or [4, 9]

nums1_3 = [1, 2, 3]
nums2_3 = [4, 5, 6]
print("nums1 =", nums1_3)
print("nums2 =", nums2_3)
print("intersection =", intersection(nums1_3.copy(), nums2_3.copy()))  # []

# Detailed trace for [1,2,2,1] and [2,2] (order may vary):
print("\nDetailed trace for [1,2,2,1] & [2,2]:")
seen = set([1, 2, 2, 1])  # deduplicated to {1,2}
print("seen =", seen)

res = []
for i in [2, 2]:
    print(f"i={i}, in seen? {i in seen}")
    if i in seen:
        res.append(i)
        seen.remove(i)
        print(f"  → res = {res}, seen = {seen} after remove")
print("Final result =", res)