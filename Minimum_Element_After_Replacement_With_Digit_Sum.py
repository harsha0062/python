from typing import List
from math import inf

def minElement(nums: List[int]) -> int:
    """
    Replace each number in `nums` with the sum of its digits,
    then return the minimum value among all these digit sums.

    For each number i:
        - Compute sum of its digits by repeatedly taking i % 10 and i // 10.
        - Track the minimum digit sum seen so far.

    Returns the minimum digit sum.
    """
    result = inf  # Initialize with infinity

    for i in nums:
        digit_sum = 0
        while i > 0:
            digit_sum += i % 10   # add last digit
            i //= 10              # remove last digit

        result = min(result, digit_sum)

    return result


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
nums1 = [10, 12, 13, 14]
print("nums1 =", nums1)
print("minElement =", minElement(nums1))  # min digit sum

nums2 = [1, 2, 3]
print("\nnums2 =", nums2)
print("minElement =", minElement(nums2))  # 1

nums3 = [99, 9, 18, 27]
print("\nnums3 =", nums3)
print("minElement =", minElement(nums3))

# Visualize digit sums for nums3
print("\nDigit sum breakdown for nums3:")
for x in nums3:
    n = x
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    print(f"  {x} → digit sum = {s}")