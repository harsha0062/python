from typing import List
from bisect import bisect_left

def gcdValues(nums: List[int], queries: List[int]) -> List[int]:
    """
    Return the gcd value at each query index after listing all pair GCDs
    in sorted order.
    """
    mx = max(nums)

    # arr[x] will be used to count how many pairs have gcd exactly x
    arr = [0] * (mx + 1)

    # Count frequency of each number
    for n in nums:
        arr[n] += 1

    # Step 1: For each i, count how many numbers are divisible by i
    # After this loop, arr[i] becomes the count of numbers divisible by i
    for i in range(1, mx + 1):
        for j in range(i * 2, mx + 1, i):
            arr[i] += arr[j]

    # Step 2: Number of pairs where both numbers are divisible by i
    for i in range(1, mx + 1):
        arr[i] = arr[i] * (arr[i] - 1) // 2

    # Step 3: Inclusion-exclusion to get count of pairs with gcd exactly i
    for i in range(mx, 0, -1):
        for j in range(i * 2, mx + 1, i):
            arr[i] -= arr[j]

    # Step 4: Prefix sum so we can binary search answers for queries
    for i in range(1, mx + 1):
        arr[i] += arr[i - 1]

    res = []
    for q in queries:
        idx = bisect_left(arr, q + 1)
        res.append(idx)

    return res


# Input inside the code
nums = [2, 3, 4, 6, 8]
queries = [0, 1, 2, 3, 4, 5]

print(gcdValues(nums, queries))