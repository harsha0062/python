from typing import List

def canReach(s: str, minJump: int, maxJump: int) -> bool:
    """
    Determine whether you can jump from index 0 to the last index of binary string s,
    following these rules:
        - You start at index 0 (which is guaranteed to be '0').
        - From index i, you can jump to index j if:
            1. i + minJump <= j <= i + maxJump
            2. j is within [0, n-1]
            3. s[j] == '0' (you can only land on '0').

    Uses DP:
        - dp[i] = True means index i is reachable.
        - dp[0] = True (start).
        - For each index i where dp[i] is True, we mark all valid j in [i+minJump, i+maxJump] as reachable
          if s[j] == '0'.
    """
    n = len(s)
    # dp[i] is True if index i is reachable
    dp = [False] * n
    dp[0] = True      # start position is reachable

    # last marks the rightmost position that has been processed in a previous jump interval
    last = 0

    for i in range(n):
        # If current index is not reachable, skip
        if not dp[i]:
            continue

        # Compute the valid jump range from position i
        l = max(i + minJump, last + 1)   # avoid reprocessing already marked indices
        h = min(i + maxJump, n - 1)      # cannot exceed last index

        # If interval [l, h] is valid...
        if l <= h:
            for j in range(l, h + 1):
                if s[j] == '0':
                    dp[j] = True
            # Remember the rightmost covered index to avoid duplicate work in next step
            last = h

    # Return whether the last index is reachable
    return dp[-1]


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
s1 = "011010"
minJump1 = 2
maxJump1 = 3
print("s =", s1)
print("minJump =", minJump1, ", maxJump =", maxJump1)
print("canReach =", canReach(s1, minJump1, maxJump1))  # True (example 1871)

s2 = "0110"
minJump2 = 2
maxJump2 = 3
print("\ns =", s2)
print("minJump =", minJump2, ", maxJump =", maxJump2)
print("canReach =", canReach(s2, minJump2, maxJump2))  # False

s3 = "0000000000"
minJump3 = 2
maxJump3 = 5
print("\ns =", s3)
print("minJump =", minJump3, ", maxJump =", maxJump3)
print("canReach =", canReach(s3, minJump3, maxJump3))  # True (fully connected 0s)

s4 = "0101010101"
minJump4 = 1
maxJump4 = 1
print("\ns =", s4)
print("minJump =", minJump4, ", maxJump =", maxJump4)
print("canReach =", canReach(s4, minJump4, maxJump4))  # Depends; jumps = 1 => 0→1 OK, but 1→0 OK;
# checks each step up to last if 0

# Visualize propagation for s="011010", minJump=2, maxJump=3
print("\nTrace for s='011010', minJump=2, maxJump=3:")
dp = [False]*6
dp[0] = True
print("Start:", dp)  # [True, False, False, False, False, False]

last = 0
for i in range(6):
    if dp[i]:
        print(f"From index {i}: dp[{i}] = True")
        l = max(i+2, last+1)
        h = min(i+3, 5)
        print(f"  jump range: l={l}, h={h}")
        if l <= h:
            for j in range(l, h+1):
                if s1[j] == '0':
                    dp[j] = True
                    print(f"    dp[{j}] = True")
            last = h
print("Final dp =", dp)
print("dp[-1] =", dp[-1])