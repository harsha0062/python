from typing import List

def constructTransformedArray(nums: List[int]) -> List[int]:
    """
    Constructs a transformed array where each position i gets the value from index (nums[i] + i) % len(nums).
    
    Args:
        nums: Input list of integers
    
    Returns:
        List of integers with transformed values based on the formula
    """
    res = []
    for i in range(0, len(nums)):
        index = (nums[i] + i) % len(nums)  # Calculate new index using modulo for wrap-around
        res.append(nums[index])            # Place value from calculated index into result
    return res

# Input example inside the code
nums = [2, 6, 3, 5, 1]  # Example input array

# Call the function and print result
result = constructTransformedArray(nums)
print(f"Input: {nums}")
print(f"Output: {result}")
