from typing import List
from math import inf

def minSumOfLengths(arr: List[int], target: int) -> int:
    # Get the length of the array
    n = len(arr)

    # Store the current window sum
    ps = 0

    # Store the minimum total length of two valid subarrays
    res = inf

    # dp[i] stores the shortest valid subarray length
    # ending at or before index i
    dp = [inf] * n

    # Left boundary of the sliding window
    l = 0

    # Expand the window using the right boundary
    for r in range(n):
        ps += arr[r]

        # Shrink the window while its sum is greater than target
        while ps > target:
            ps -= arr[l]
            l += 1

        # Carry forward the best valid subarray found so far
        dp[r] = dp[r - 1] if r - 1 >= 0 else inf

        # If the current window has the target sum
        if ps == target:
            current_length = r - l + 1

            # Combine it with the best non-overlapping subarray
            # that ends before the current window starts
            previous_length = dp[l - 1] if l - 1 >= 0 else inf
            res = min(res, current_length + previous_length)

            # Update the best subarray length up to index r
            dp[r] = min(dp[r], current_length)

    # Return -1 if two valid subarrays were not found
    return -1 if res == inf else res


# Input inside the code
arr = [3, 2, 2, 4, 3]
target = 3

print(minSumOfLengths(arr, target))