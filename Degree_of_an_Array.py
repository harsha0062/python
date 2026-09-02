from typing import List

def findShortestSubArray(nums: List[int]) -> int:
    # Store frequency, first occurrence, and last occurrence of each number
    count = {}
    start = {}
    end = {}

    for i in range(len(nums)):
        if nums[i] not in count:
            count[nums[i]] = 1
            start[nums[i]] = i
            end[nums[i]] = i
        else:
            count[nums[i]] += 1
            end[nums[i]] = i

    # Find the maximum frequency (degree of the array)
    maxi = max(count.values())

    # Collect lengths of smallest subarrays for all elements with max frequency
    res = []
    for num, freq in count.items():
        if freq == maxi:
            total = end[num] - start[num] + 1
            res.append(total)

    # Return the smallest length among them
    return min(res)


# Input inside the code
nums = [1, 2, 2, 3, 1]

print(findShortestSubArray(nums))