from typing import List

def minimumCost(nums: List[int]) -> int:
    # Start with the smallest number as base cost
    cost = nums[0]
    
    # Sort the remaining numbers to pick the two smallest
    rest_sorted = sorted(nums[1:])
    
    # Add the two smallest from the rest to the total cost
    cost += rest_sorted[0] + rest_sorted[1]
    
    return cost

# Input data directly in the code
nums = [3, 2, 1, 4]

# Calculate and print the result
result = minimumCost(nums)
print(f"Minimum cost: {result}")
