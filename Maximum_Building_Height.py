from typing import List

def maxBuilding(n: int, restrictions: List[List[int]]) -> int:
    """
    Compute the maximum possible height of any building in a line of n buildings,
    given restrictions on the maximum height of certain buildings.

    Constraints:
      - Building indices are 1 to n.
      - Building 1 must have height 0.
      - The height difference between adjacent buildings cannot exceed 1.
      - Each restriction [i, h] means building i's height ≤ h.

    Algorithm (three passes):
      1. Add restrictions:
         - Building 1 must be height 0 → add [1, 0].
         - If building n is not restricted, add [n, n-1] (maximum possible height for building n).
      2. Sort restrictions by building index.
      3. Forward pass (left to right):
         - For each restriction i, ensure its height respects the previous restriction:
           height[i] ≤ height[i-1] + distance(i-1, i)
      4. Backward pass (right to left):
         - For each restriction i, ensure its height respects the next restriction:
           height[i] ≤ height[i+1] + distance(i, i+1)
      5. Final pass:
         - For each adjacent pair of restricted buildings (i-1, i) with heights h1, h2
           and distance d = pos[i] - pos[i-1], the maximum achievable height between them is:
             curr = (d + h1 + h2) // 2
         - Track the maximum such value.

    Returns:
        The maximum possible building height.
    """
    # Add mandatory restrictions
    restrictions.append([1, 0])
    restrictions.sort()

    # If building n is not restricted, add its maximum possible height
    if restrictions[-1][0] != n:
        restrictions.append([n, n - 1])

    r = len(restrictions)

    # Forward pass: left to right
    for i in range(1, r):
        dist = restrictions[i][0] - restrictions[i - 1][0]
        restrictions[i][1] = min(restrictions[i][1], dist + restrictions[i - 1][1])

    # Backward pass: right to left
    for i in range(r - 2, -1, -1):
        dist = restrictions[i + 1][0] - restrictions[i][0]
        restrictions[i][1] = min(restrictions[i][1], dist + restrictions[i + 1][1])

    # Final pass: compute maximum height between adjacent restrictions
    res = 0
    for i in range(1, r):
        dist = restrictions[i][0] - restrictions[i - 1][0]
        h1, h2 = restrictions[i - 1][1], restrictions[i][1]
        # Max height between these two buildings
        curr = (dist + h1 + h2) // 2
        res = max(res, curr)

    return res


# Test cases with inputs inside code (no `if __name__ == "__main__"`)
n1 = 5
restrictions1 = [[2, 1], [4, 3]]
print("n1 =", n1)
print("restrictions1 =", restrictions1)
print("maxBuilding =", maxBuilding(n1, restrictions1.copy()))
# Expected: 3

n2 = 6
restrictions2 = []
print("\nn2 =", n2)
print("restrictions2 =", restrictions2)
print("maxBuilding =", maxBuilding(n2, restrictions2.copy()))
# Expected: 4 (building 1 = 0, then 1,2,3,4)

n3 = 10
restrictions3 = [[5, 3], [2, 1], [7, 2]]
print("\nn3 =", n3)
print("restrictions3 =", restrictions3)
print("maxBuilding =", maxBuilding(n3, restrictions3.copy()))

# Detailed trace for n=5, restrictions=[[2,1],[4,3]]
print("\nDetailed trace for n=5, restrictions=[[2,1],[4,3]]:")
n = 5
restrictions = [[2, 1], [4, 3]]

# Add restrictions
restrictions.append([1, 0])
restrictions.sort()
print("After adding [1,0] and sorting:", restrictions)

if restrictions[-1][0] != n:
    restrictions.append([n, n - 1])
print("After potentially adding [n, n-1]:", restrictions)

r = len(restrictions)

# Forward pass
print("\nForward pass (left to right):")
for i in range(1, r):
    dist = restrictions[i][0] - restrictions[i - 1][0]
    old_h = restrictions[i][1]
    restrictions[i][1] = min(old_h, dist + restrictions[i - 1][1])
    print(f"  i={i}: pos={restrictions[i][0]}, old_h={old_h}, dist={dist}, prev_h={restrictions[i-1][1]}, new_h={restrictions[i][1]}")

# Backward pass
print("\nBackward pass (right to left):")
for i in range(r - 2, -1, -1):
    dist = restrictions[i + 1][0] - restrictions[i][0]
    old_h = restrictions[i][1]
    restrictions[i][1] = min(old_h, dist + restrictions[i + 1][1])
    print(f"  i={i}: pos={restrictions[i][0]}, old_h={old_h}, dist={dist}, next_h={restrictions[i+1][1]}, new_h={restrictions[i][1]}")

# Final pass
print("\nFinal pass (compute max height between adjacent restrictions):")
res = 0
for i in range(1, r):
    dist = restrictions[i][0] - restrictions[i - 1][0]
    h1, h2 = restrictions[i - 1][1], restrictions[i][1]
    curr = (dist + h1 + h2) // 2
    res = max(res, curr)
    print(f"  i={i}: pos_left={restrictions[i-1][0]}, h1={h1}, pos_right={restrictions[i][0]}, h2={h2}, dist={dist}, curr={curr}, res={res}")

print("\nFinal result:", res)