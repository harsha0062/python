from typing import List

# Function to find the element repeated N times
def repeatedNTimes(nums: List[int]) -> int:
    d = {}  # dictionary to store frequency of each number

    # Count frequency of each number
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    # Find the key with maximum value (maximum frequency)
    k = max(d, key=d.get)

    return k


# ---- INPUT GIVEN INSIDE THE CODE ----
nums = [1, 2, 3, 3]

# Function call
result = repeatedNTimes(nums)

# Output
print("Repeated element:", result)
