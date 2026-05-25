from typing import List
from functools import cache

# ----------------------------------------------------------------
# METHOD 1: DFS + EXPLICIT MEMO DICT (seen dict style)
# ----------------------------------------------------------------
def maxJumps_method1(arr: List[int], d: int) -> int:
    """
    Maximum number of indices you can visit starting from any index.

    Rules:
      - From index i you may jump to index j if:
          1. 0 <= j < len(arr)
          2. |i - j| <= d
          3. arr[i] > arr[j] (only strictly lower values)
      - You can visit as many indices as possible along the path.

    Uses:
      - DFS with explicit memoization in `seen` dict.
      - `seen[pos]` stores the maximum number of indices reachable starting at `pos` (including `pos`).

    Algorithm sketch:
      1. For each starting index `i`, call `dfs(i)`.
      2. In `dfs(pos)`:
           - Mark `pos` as visited, `seen[pos] = 1`.
           - Go left and right within distance `d`.
           - For each valid `i` (lower value), recurse `dfs(i)`.
           - Then: seen[pos] = max(seen[pos], seen[i] + 1).
      3. Answer = max(seen.values()).
    """
    seen = dict()  # position -> maximum number of indices reachable from that position

    def dfs(pos: int) -> None:
        # If already computed, skip.
        if pos in seen:
            return

        # At least 1 (the current index itself).
        seen[pos] = 1

        # Left direction: pos-1, pos-2, ... within distance d
        i = pos - 1
        while i >= 0 and pos - i <= d and arr[pos] > arr[i]:
            dfs(i)              # compute value for i first
            if i in seen:       # ensure i is in memo
                seen[pos] = max(seen[pos], seen[i] + 1)
            i -= 1

        # Right direction: pos+1, pos+2, ... within distance d
        i = pos + 1
        while i < len(arr) and i - pos <= d and arr[pos] > arr[i]:
            dfs(i)
            if i in seen:
                seen[pos] = max(seen[pos], seen[i] + 1)
            i += 1

    # Compute max jumps starting from every index
    for i in range(len(arr)):
        dfs(i)

    # If no indices visited, return 0 (but arr is non‑empty, so this is just safety)
    return max(seen.values()) if seen else 0


# ----------------------------------------------------------------
# METHOD 2: DFS + @cache (functional DP style)
# ----------------------------------------------------------------
def maxJumps_method2(arr: List[int], d: int) -> int:
    """
    Same problem as method1, but reimplemented using:
      - `@cache` instead of a manual dict `seen`.
      - `dfs(i)` returns an integer (the maximum path length starting at `i`).

    Rules:
      - Same jump rules as above.

    Algorithm:
      1. `dfs(i)`:
           - Start with res = 1 (only index i).
           - To the right: try j = i+1, i+2, ..., i+d.
                 * if arr[j] >= arr[i]: stop this direction (cannot jump)
                 * else: res = max(res, dfs(j) + 1)
           - To the left: try j = i-1, i-2, ..., i-d.
                 * if arr[j] >= arr[i]: stop.
                 * else: res = max(res, dfs(j) + 1).
           - Return res.
      2. For each i in [0, n-1], compute dfs(i) and track the maximum.
    """
    n = len(arr)

    @cache
    def dfs(i: int) -> int:
        res = 1  # at least the current index

        # RIGHT: from i+1 up to i + d (but stay in bounds)
        right_end = min(i + d + 1, n)
        for j in range(i + 1, right_end):
            if arr[j] >= arr[i]:
                break  # cannot jump over equal or higher value
            res = max(res, dfs(j) + 1)

        # LEFT: from i-1 down to i - d (but stay ≥ 0)
        left_end = max(i - d - 1, -1)
        for j in range(i - 1, left_end, -1):
            if arr[j] >= arr[i]:
                break
            res = max(res, dfs(j) + 1)

        return res

    res = 1
    for i in range(n):
        res = max(res, dfs(i))

    return res


# ----------------------------------------------------------------
# TEST CASES (inputs written inside code)
# ----------------------------------------------------------------

# Example 1
arr1 = [6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12]
d1 = 2
print("Example 1:")
print("arr1 =", arr1)
print("d1 =", d1)
print("Method 1 result:", maxJumps_method1(arr1.copy(), d1))  # 4
print("Method 2 result:", maxJumps_method2(arr1.copy(), d1))  # 4

# Example 2: all equal values
arr2 = [3, 3, 3, 3, 3]
d2 = 3
print("\nExample 2:")
print("arr2 =", arr2)
print("d2 =", d2)
print("Method 1 result:", maxJumps_method1(arr2.copy(), d2))  # 1
print("Method 2 result:", maxJumps_method2(arr2.copy(), d2))  # 1

# Example 3: strictly decreasing
arr3 = [7, 6, 5, 4, 3, 2, 1]
d3 = 1
print("\nExample 3:")
print("arr3 =", arr3)
print("d3 =", d3)
print("Method 1 result:", maxJumps_method1(arr3.copy(), d3))  # 7
print("Method 2 result:", maxJumps_method2(arr3.copy(), d3))  # 7

# Example 4: alternating 7,1,7,1,...
arr4 = [7, 1, 7, 1, 7, 1]
d4 = 2
print("\nExample 4:")
print("arr4 =", arr4)
print("d4 =", d4)
print("Method 1 result:", maxJumps_method1(arr4.copy(), d4))  # 2
print("Method 2 result:", maxJumps_method2(arr4.copy(), d4))  # 2