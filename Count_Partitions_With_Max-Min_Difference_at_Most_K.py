from typing import List
from sortedcontainers import SortedList  # pip install sortedcontainers

# Same function body as you provided
def countPartitions(nums: List[int], k: int) -> int:
    mod = 10**9 + 7
    n = len(nums)
    
    # dp[i] = number of ways to partition first i elements (nums[0..i-1])
    dp = [1] + [0] * n
    
    # acc = prefix sum of dp values over current valid window
    acc = 1
    
    # SortedList to maintain current window elements in sorted order
    sl = SortedList()
    
    l = 0  # left pointer of sliding window
    for r in range(n):
        # Add current element to the window
        sl.add(nums[r])
        
        # Shrink window from left while max - min > k
        while sl[-1] - sl[0] > k:
            sl.remove(nums[l])
            acc = (acc - dp[l]) % mod  # remove contribution of dp[l]
            l += 1
        
        # dp[r+1] = sum of dp[l..r] (stored in acc)
        dp[r + 1] = acc
        
        # Update acc to include new dp[r+1] for future positions
        acc = (acc + dp[r + 1]) % mod
    
    # Answer: number of ways to partition all n elements
    return dp[n]

# Example input inside the code
nums = [9, 4, 1, 3, 7]  # sample array
k = 4                   # sample k

# Call the function and print the result
ans = countPartitions(nums, k)
print(ans)
