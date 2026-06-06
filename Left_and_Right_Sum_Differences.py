from typing import List

def leftRightDifference(nums: List[int]) -> List[int]:
    """
    Compute the absolute difference between left and right sums for each index.

    For each index i:
        - left sum = sum of all elements to the left of i (nums[0]..nums[i-1])
        - right sum = sum of all elements to the right of i (nums[i+1]..nums[n-1])
        - result[i] = abs(left sum - right sum)

    Approach:
        - Start with:
            left = 0
            right = sum(nums)  (total sum initially)
        - For each index i from 0 to n-1:
            * If i > 0, add nums[i-1] to left (element just left of current).
            * Remove nums[i] from right (since right should not include current element).
            * Append abs(left - right) to result.
    """
    res = []
    left = 0
    right = sum(nums)  # initial right sum is the total sum

    for i in range(len(nums)):
        if i > 0:
            left += nums[i - 1]  # add element to the left of current index

        right -= nums[i]         # remove current element from right sum

        res.append(abs(left - right))

    return res


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
nums1 = [1, 2, 3, 4]
print("nums1 =", nums1)
print("leftRightDifference =", leftRightDifference(nums1))
# i=0: left=0, right=9 → |0-9|=9
# i=1: left=1, right=7 → |1-7|=6
# i=2: left=3, right=4 → |3-4|=1
# i=3: left=6, right=0 → |6-0|=6

nums2 = [1, 1, 1, 1]
print("\nnums2 =", nums2)
print("leftRightDifference =", leftRightDifference(nums2))
# i=0: left=0, right=3 → 3
# i=1: left=1, right=2 → 1
# i=2: left=2, right=1 → 1
# i=3: left=3, right=0 → 3

nums3 = [5]
print("\nnums3 =", nums3)
print("leftRightDifference =", leftRightDifference(nums3))
# i=0: left=0, right=0 → 0

# Step-by-step trace for nums1
print("\nTrace for nums1 = [1, 2, 3, 4]:")
nums = [1, 2, 3, 4]
left = 0
right = sum(nums)
print(f"Initial: left={left}, right={right}")
for i in range(len(nums)):
    if i > 0:
        left += nums[i - 1]
    right -= nums[i]
    diff = abs(left - right)
    print(f"i={i}: left={left}, right={right}, |left-right|={diff}")