from typing import List

def minMoves(nums: List[int], limit: int) -> int:
    """
    Minimum moves to make nums complementary: nums[i] + nums[n-1-i] >= limit for all i.
    Use difference array (sweep line) on possible target sums T=2 to 2*limit.
    For each pair (a,b), update delta where T makes pair complementary or not.
    """
    n = len(nums)
    dif = [0] * (2 * limit + 2)  # delta array for sweep line
    
    # Process pairs nums[i] + nums[n-1-i]
    for i in range(n // 2):
        l = nums[i]
        r = nums[n - 1 - i]
        
        # For target T:
        dif[min(l, r) + 1] -= 1     # T > min(l,r): both need change if T <= l+r
        dif[l + r] -= 1              # T == l+r: one needs change  
        dif[l + r + 1] += 1          # T > l+r: both need change
        dif[max(l, r) + limit + 1] += 1  # T > max(l,r)+limit: optimization boundary
    
    res, curr = n, n              # Initial moves = n (change one per pair)
    for i in range(2, 2 * limit + 1):  # Sweep possible target sums T
        curr += dif[i]             # Update moves needed for target=i
        res = min(res, curr)       # Track minimum moves
    
    return res


# Test cases with inputs inside code
print("nums=[1,2,4,7], limit=7 ->", minMoves([1,2,4,7], 7))  # Expected: 2
print("nums=[1,10,11,9], limit=18 ->", minMoves([1,10,11,9], 18))  # Expected: 2

# Visualize difference array effect:
print("\nDifference array visualization for nums=[1,2,4,7], limit=7:")
nums = [1,2,4,7]; limit = 7
pairs = [(nums[i], nums[3-i]) for i in range(2)]
print("Pairs:", pairs)

dif = [0] * (2*limit + 2)
for l, r in pairs:
    print(f"Pair ({l},{r}):")
    print(f"  dif[{min(l,r)+1}] -=1")
    print(f"  dif[{l+r}] -=1") 
    print(f"  dif[{l+r+1}] +=1")
    print(f"  dif[{max(l,r)+limit+1}] +=1\n")
    
    dif[min(l, r) + 1] -= 1
    dif[l + r] -= 1
    dif[l + r + 1] += 1
    dif[max(l, r) + limit + 1] += 1

print("Cumulative moves:")
res, curr = 4, 4
print(f"T=2: moves={curr}")
for i in range(2, 15):
    curr += dif[i]
    print(f"T={i}: moves={curr}, delta={dif[i]}")
    res = min(res, curr)
print(f"Minimum moves: {res}")