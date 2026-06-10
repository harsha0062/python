from typing import List
from math import inf
import heapq

# ----------------------------------------------------------------
# Segment Tree ST
# Supports:
#   - build: construct tree where each node stores (max, min) of its range
#   - query(ql, qr): return (max, min) in range [ql, qr]
# ----------------------------------------------------------------
class ST:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.n = len(arr)
        # Each node stores (max_value, min_value) for its range
        self.st = [(0, 0) for _ in range(4 * self.n)]
        self.build(1, 0, self.n - 1)

    def build(self, node: int, l: int, r: int) -> None:
        """
        Build the segment tree.
        Each node stores:
          - first element: maximum in range [l, r]
          - second element: minimum in range [l, r]
        """
        if l == r:
            # Leaf node: both max and min are the element itself
            self.st[node] = (self.arr[l], self.arr[l])
            return

        mid = l + (r - l) // 2
        self.build(2 * node, l, mid)
        self.build(2 * node + 1, mid + 1, r)

        # Combine children: max from left/right, min from left/right
        self.st[node] = (
            max(self.st[2 * node][0], self.st[2 * node + 1][0]),
            min(self.st[2 * node][1], self.st[2 * node + 1][1])
        )

    def query(self, ql: int, qr: int, node: int = 1, l: int = 0, r: int = None) -> tuple:
        """
        Query the maximum and minimum in range [ql, qr].
        Returns (max_value, min_value).
        """
        if r is None:
            r = self.n - 1

        # No overlap
        if ql > r or qr < l:
            return (-inf, inf)

        # Total overlap
        if ql <= l and qr >= r:
            return self.st[node]

        mid = l + (r - l) // 2
        lmx, lmn = self.query(ql, qr, 2 * node, l, mid)
        rmx, rmn = self.query(ql, qr, 2 * node + 1, mid + 1, r)

        return (
            max(lmx, rmx),
            min(lmn, rmn)
        )


# ----------------------------------------------------------------
# maxTotalValue(nums, k):
#
# Problem idea (based on the code):
#   - You can choose up to k subarrays.
#   - For each chosen subarray [l, r], you get value = (max - min) in that subarray.
#   - When you pick a subarray, you can then "split" it by:
#        * considering [l+1, r] (drop leftmost element)
#        * considering [l, r-1] (drop rightmost element)
#   - Use a max-heap to always pick the subarray with the largest (max - min).
#   - Track seen ranges to avoid duplicates.
#
# Algorithm:
#   1. Build segment tree over nums for O(log n) max/min queries.
#   2. Start with the full range [0, n-1], push it into heap with key = -(max - min).
#   3. While k > 0 and heap not empty:
#        - Pop the subarray with largest (max - min).
#        - Add that value to result.
#        - Push [l+1, r] and [l, r-1] if they are valid and not seen.
#   4. Return total result.
# ----------------------------------------------------------------
def maxTotalValue(nums: List[int], k: int) -> int:
    n = len(nums)
    st = ST(nums)
    mh = []  # max-heap (using negative values with heapq)

    # Initial range: full array [0, n-1]
    mx, mn = st.query(0, n - 1)
    heapq.heappush(mh, (-(mx - mn), 0, n - 1))

    seen = set()
    seen.add((0, n - 1))

    res = 0

    while k > 0 and mh:
        k -= 1
        v, l, r = heapq.heappop(mh)
        v = -v  # convert back to positive value
        res += v

        # Option 1: shrink from left → [l+1, r]
        if l + 1 <= r and (l + 1, r) not in seen:
            mx, mn = st.query(l + 1, r)
            heapq.heappush(mh, (-(mx - mn), l + 1, r))
            seen.add((l + 1, r))

        # Option 2: shrink from right → [l, r-1]
        if l <= r - 1 and (l, r - 1) not in seen:
            mx, mn = st.query(l, r - 1)
            heapq.heappush(mh, (-(mx - mn), l, r - 1))
            seen.add((l, r - 1))

    return res


# ----------------------------------------------------------------
# Test cases with inputs inside code (no `if __name__ == "__main__"`)
# ----------------------------------------------------------------
nums1 = [1, 3, 2, 5, 4]
k1 = 3
print("nums1 =", nums1)
print("k1 =", k1)
print("maxTotalValue =", maxTotalValue(nums1, k1))

nums2 = [1, 2, 3, 4, 5]
k2 = 2
print("\nnums2 =", nums2)
print("k2 =", k2)
print("maxTotalValue =", maxTotalValue(nums2, k2))

nums3 = [5, 5, 5, 5]
k3 = 3
print("\nnums3 =", nums3)
print("k3 =", k3)
print("maxTotalValue =", maxTotalValue(nums3, k3))
# All ranges have max-min = 0, so total = 0

# Detailed trace for nums1, k=3
print("\nDetailed trace for nums1=[1,3,2,5,4], k=3:")
arr = [1, 3, 2, 5, 4]
k = 3
st = ST(arr)
mh = []
seen = set()

mx, mn = st.query(0, len(arr) - 1)
heapq.heappush(mh, (-(mx - mn), 0, len(arr) - 1))
seen.add((0, len(arr) - 1))

res = 0
print(f"Initial range [0,4]: max={mx}, min={mn}, value={mx-mn}")

while k > 0 and mh:
    k -= 1
    v, l, r = heapq.heappop(mh)
    v = -v
    res += v
    print(f"Step {k+1}: picked [{l},{r}], value={v}, total={res}")

    if l + 1 <= r and (l + 1, r) not in seen:
        mx1, mn1 = st.query(l + 1, r)
        heapq.heappush(mh, (-(mx1 - mn1), l + 1, r))
        seen.add((l + 1, r))
        print(f"  → added [{l+1},{r}]: max={mx1}, min={mn1}, value={mx1-mn1}")

    if l <= r - 1 and (l, r - 1) not in seen:
        mx2, mn2 = st.query(l, r - 1)
        heapq.heappush(mh, (-(mx2 - mn2), l, r - 1))
        seen.add((l, r - 1))
        print(f"  → added [{l},{r-1}]: max={mx2}, min={mn2}, value={mx2-mn2}")

print(f"Final result: {res}")