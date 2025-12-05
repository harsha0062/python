from typing import List

# Your function (unchanged)
def countPartitions(nums: List[int]) -> int:
    # Return number of partitions with even sum difference
    # Logic: If total sum is even, every split point (n - 1 ways) works; otherwise 0
    return len(nums) - 1 if sum(nums) % 2 == 0 else 0

# Example input inside the code
nums = [1, 2, 3, 4]

# Call the function and print the result
result = countPartitions(nums)
print(result)
