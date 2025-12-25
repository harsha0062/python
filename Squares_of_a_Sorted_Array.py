# Import List type for type hinting
from typing import List

# Do not change this function (as requested)
def sortedSquares(nums: List[int]) -> List[int]:
    # Create an empty list to store squares
    s = []
    j = 0  # This variable is not used, but kept to avoid changing your code

    # Loop through each element in nums
    for i in nums:
        # Append square of current element to list s
        s.append(i * i)

    # Sort the list of squares in non-decreasing order
    s.sort()

    # Return the sorted list
    return s


# Give input inside the code (no input() and no main guard)
# Example 1
nums1 = [-4, -1, 0, 3, 10]
result1 = sortedSquares(nums1)
print("Input:", nums1)
print("Sorted squares:", result1)

# Example 2
nums2 = [-7, -3, -2, -1]
result2 = sortedSquares(nums2)
print("Input:", nums2)
print("Sorted squares:", result2)

# Example 3
nums3 = [0, 1, 2, 3]
result3 = sortedSquares(nums3)
print("Input:", nums3)
print("Sorted squares:", result3)
