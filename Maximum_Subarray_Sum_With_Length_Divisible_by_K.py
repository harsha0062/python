from typing import List

# Your original function, unchanged
def maxSubarraySum(nums: List[int], k: int) -> int:
    # pre[i] will store the minimum prefix sum seen so far
    # at indices whose length % k == i
    pre = [float("inf")] * k
    # For length % k == 0, the minimum prefix prefix sum is 0 initially
    pre[0] = 0

    # Result initialized to negative infinity so any valid sum will be larger
    res = float("-inf")

    # Running total (prefix sum)
    total = 0

    # Iterate over the array with index and value
    for i, n in enumerate(nums):
        # Update running prefix sum
        total += n

        # Current subarray length from index 0 to i is i + 1
        length = i + 1

        # Remainder of current length modulo k
        pre_len = length % k

        # Best subarray ending at i with length divisible by k:
        # subtract the minimum prefix sum of the same remainder
        res = max(res, total - pre[pre_len])

        # Update minimum prefix sum for this remainder class
        pre[pre_len] = min(pre[pre_len], total)

    return res


# Example input given directly inside the code
nums = [3, -2, 5, -1, 6, -3, 2]
k = 3

# Call the function and print the result
answer = maxSubarraySum(nums, k)
print("Maximum subarray sum with length divisible by", k, "is:", answer)
