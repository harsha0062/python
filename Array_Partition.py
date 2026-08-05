from typing import List

def arrayPairSum(nums: List[int]) -> int:
    # Sort the array so pairs can be formed optimally
    nums.sort()

    # Initialize the answer
    ans = 0

    # Traverse the array in steps of 2 and add the smaller element of each pair
    n = len(nums)
    for i in range(1, n, 2):
        ans += min(nums[i], nums[i - 1])

    return ans


# Input inside the code
nums = [1, 4, 3, 2]

print(arrayPairSum(nums))