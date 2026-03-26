def subarraySum(nums: list[int], k: int) -> int:
    """
    Count subarrays with sum exactly equal to k using prefix sum + hashmap.
    Key insight: if prefix[i] - prefix[j] = k, then subarray(j+1 to i) sums to k.
    """
    res = 0                    # Count of valid subarrays
    currSum = 0                # Running prefix sum
    prefixSums = {0: 1}        # {prefix_sum: frequency}, 0:1 handles subarrays from start
    
    for n in nums:
        currSum += n            # Update prefix sum
        
        diff = currSum - k      # Look for prefix sum that was 'k' ago
        res += prefixSums.get(diff, 0)  # Add count of such prefixes
        
        # Record current prefix sum frequency
        prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
    
    return res


# Test cases with inputs inside code
print("nums=[1,1,1], k=2 ->", subarraySum([1,1,1], 2))      # Expected: 2 ([1,1],[1,1])
print("nums=[1,2,3], k=3 ->", subarraySum([1,2,3], 3))      # Expected: 2 ([3],[1,2])
print("nums=[2,-1,1,2], k=2 ->", subarraySum([2,-1,1,2], 2)) # Expected: 4
print("nums=[0,0,0,0,0], k=0 ->", subarraySum([0,0,0,0,0], 0)) # Expected: 15

# Visualize prefix sums for [1,1,1], k=2:
print("\nStep-by-step for [1,1,1], k=2:")
nums = [1,1,1]; k = 2
prefixSums = {0: 1}
currSum = 0; res = 0

for i, n in enumerate(nums):
    currSum += n
    diff = currSum - k
    print(f"i={i}: currSum={currSum}, diff={diff}, res+={prefixSums.get(diff,0)} -> res={res}")
    res += prefixSums.get(diff, 0)
    prefixSums[currSum] = prefixSums.get(currSum, 0) + 1
print(f"Final result: {res}")
