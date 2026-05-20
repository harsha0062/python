from collections import defaultdict
from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find the intersection of two arrays, preserving duplicates up to their minimum frequency.

    Steps:
      1. Count frequency of each element in nums1 using map1.
      2. For each element in nums2:
           - Decrement its count in map1.
           - If after decrement the count is still >= 0, include it in result.
           This ensures that each value appears at most min(freq_in_nums1, freq_in_nums2) times.
    """
    map1 = defaultdict(int)  # frequency map for nums1
    result = []

    # Step 1: count nums1 frequencies
    for i in nums1:
        map1[i] += 1

    # Step 2: traverse nums2 and “consume” counts from map1
    for j in nums2:
        map1[j] -= 1
        if map1[j] >= 0:      # still has room (not oversubscribed)
            result.append(j)

    return result


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
nums1_1 = [1, 2, 2, 1]
nums2_1 = [2, 2]
print("nums1 =", nums1_1)
print("nums2 =", nums2_1)
print("intersect =", intersect(nums1_1.copy(), nums2_1.copy()))  # [2, 2]

nums1_2 = [4, 9, 5]
nums2_2 = [9, 4, 9, 8, 4]
print("nums1 =", nums1_2)
print("nums2 =", nums2_2)
print("intersect =", intersect(nums1_2.copy(), nums2_2.copy()))  # [9, 4] or [4, 9]

nums1_3 = [1, 2, 3]
nums2_3 = [4, 5, 6]
print("nums1 =", nums1_3)
print("nums2 =", nums2_3)
print("intersect =", intersect(nums1_3.copy(), nums2_3.copy()))  # []


# Step‑by‑step for nums1=[1,2,2,1], nums2=[2,2]:
print("\nDetailed trace for [1,2,2,1] & [2,2]:")
map1 = defaultdict(int)
for x in [1, 2, 2, 1]:
    map1[x] += 1
print("map1 after nums1 =", dict(map1))

result = []
for j in [2, 2]:
    print(f"Before processing {j}: map1[{j}] = {map1[j]}")
    map1[j] -= 1
    print(f"After decrement: map1[{j}] = {map1[j]}")
    if map1[j] >= 0:
        result.append(j)
        print(f"Add {j} to result = {result}")
print("Final result =", result)