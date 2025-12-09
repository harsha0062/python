from collections import defaultdict
from typing import List

# Your function (logic unchanged, only 'return ans' fixed)
def specialTriplets(nums: List[int]) -> int:
    mp = defaultdict(int)
    count = 0
    for i in nums:
        mp[i] += 1

    prefix = defaultdict(int)
    ans, mod = 0, 10**9 + 7

    for i in nums:
        total = mp[2 * i]          # how many elements equal to 2 * nums[j]
        left = prefix[2 * i]       # how many such elements are on the left side
        right = total - left       # how many such elements are on the right side

        if i == 0:                 # adjust for current element when nums[j] == 0
            right -= 1

        prefix[i] += 1             # include current element in prefix
        ans = (ans + left * right) % mod  # add number of triplets with this j

    return ans

# Example input inside the code
nums = [6, 3, 6]  # you can change this to test other cases
result = specialTriplets(nums)
print(result)
