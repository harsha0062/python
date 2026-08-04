from typing import List

def findMissingElements(nums: List[int]) -> List[int]:
    # Store all missing elements
    ans = []

    # Check every number between the minimum and maximum values
    # The maximum value is excluded because the original function uses range()
    for i in range(min(nums), max(nums)):
        # Add the number if it does not exist in nums
        if i not in nums:
            ans.append(i)

    return ans


# Input inside the code
nums = [1, 2, 3, 5]

print(findMissingElements(nums))