from typing import List

# Function to return the k most frequent elements from the list.
# Your original logic is kept exactly the same.
def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Dictionary to store frequency of each number.
    m = {}
    for i in nums:
        # If element already present, increase its count.
        if i in m:
            m[i] += 1
        # If element seen first time, initialize its count as 1.
        else:
            m[i] = 1

    # Sort keys of dictionary by their frequency in descending order.
    sorted_keys = sorted(m, key=lambda x: m[x], reverse=True)

    # Return first k keys (top k frequent elements).
    return sorted_keys[:k]


# --------------- Sample input inside the code ---------------

# Example input array and k value.
nums = [1, 1, 1, 2, 2, 3]   # You can change this list to test other cases.
k = 2                       # You can change k as needed.

# Call the function with the sample input.
result = topKFrequent(nums, k)

# Print the result.
print("Input nums:", nums)
print("k:", k)
print("Top k frequent elements:", result)
