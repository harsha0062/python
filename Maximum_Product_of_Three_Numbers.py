from typing import List

def maximumProduct(nums: List[int]) -> int:
    # Sort the array in ascending order
    nums.sort()

    # Maximum product can be:
    # 1) product of the three largest numbers
    # 2) product of the two smallest numbers and the largest number
    return max(nums[-3] * nums[-2] * nums[-1], nums[0] * nums[1] * nums[-1])


# Input inside the code
nums = [1, 2, 3, 4]

print(maximumProduct(nums))