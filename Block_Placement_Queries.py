from typing import List
from sortedcontainers import SortedList

# Maximum value for coordinates (as given in the original code)
MX = 10**5


# ----------------------------------------------------------------
# Segment Tree for Range Maximum Query
# Supports:
#   - insert(idx, val): set position idx to value val
#   - check(ql, qr): maximum value in range [ql, qr]
# ----------------------------------------------------------------
class ST:
    def __init__(self):
        # Size: 4 * (MX + 1) is safe for segment tree over [0, MX]
        self.st = [0] * (4 * (MX + 1))

    def insert(self, idx: int, val: int, node: int = 1, l: int = 0, r: int = MX) -> None:
        """
        Set value at position `idx` to `val`.
        After updating the leaf, propagate up by taking max of children.
        """
        if l == r:
            self.st[node] = val
            return

        mid = l + (r - l) // 2
        if idx <= mid:
            self.insert(idx, val, node * 2, l, mid)
        else:
            self.insert(idx, val, node * 2 + 1, mid + 1, r)

        # Update current node as max of its two children
        self.st[node] = max(self.st[node * 2], self.st[node * 2 + 1])

    def check(self, ql: int, qr: int, node: int = 1, l: int = 0, r: int = MX) -> int:
        """
        Query maximum value in range [ql, qr].
        Standard segment tree range maximum query.
        """
        # No overlap
        if r < ql or l > qr:
            return 0

        # Total overlap
        if ql <= l and qr >= r:
            return self.st[node]

        mid = l + (r - l) // 2

        # Query both children and take max
        left_max = self.check(ql, qr, node * 2, l, mid)
        right_max = self.check(ql, qr, node * 2 + 1, mid + 1, r)
        return max(left_max, right_max)


# ----------------------------------------------------------------
# Main function: process queries on a line with obstacles.
#
# We maintain:
#   - obs: a sorted list of obstacle positions (initially [0, MX])
#   - st: a segment tree that stores, for each obstacle position l,
#         the length of the gap to the next obstacle (i.e., r - l).
#
# Query types:
#   1. [1, x]: add an obstacle at position x.
#      - Find the current interval [l, r] containing x (l < x < r).
#      - Replace gap (r - l) with two gaps: (x - l) and (r - x).
#      - Update segment tree accordingly.
#   2. [2, x, sz]: check if there exists a gap of length >= sz
#      to the left of x (i.e., in the region before x).
#      - Find the interval [l, r] that contains x (l < x < r).
#      - Check maximum gap in [0, r-1] using segment tree.
#      - Also consider the tail gap from r to x (i.e., x - r).
#      - Return whether max(gap_left, tail) >= sz.
# ----------------------------------------------------------------
def getResults(queries: List[List[int]]) -> List[bool]:
    res = []

    # Sorted list of obstacle positions, initially at 0 and MX
    obs = SortedList([0, MX])

    # Segment tree over [0, MX]
    st = ST()

    # Initially, the only gap is from 0 to MX, so we record that at position 0
    st.insert(0, MX)

    for q in queries:
        if q[0] == 1:
            # Add obstacle at position x
            _, x = q

            # Find the position where x would be inserted
            i = obs.bisect_left(x)

            # Current interval containing x: (obs[i-1], obs[i])
            l, r = obs[i - 1], obs[i]

            # Remove the old gap (l, r) and add two new gaps:
            #   - (l, x) with length x - l
            #   - (x, r) with length r - x
            # We represent gaps by storing at position l the length to the next obstacle.
            st.insert(l, x - l)
            st.insert(x, r - x)

            # Insert x into the obstacle list
            obs.add(x)

        else:
            # Query: check if there is a gap of length >= sz before position x
            _, x, sz = q

            # Find interval containing x
            i = obs.bisect_left(x)
            l, r = obs[i - 1], obs[i]

            # Query maximum gap in range [0, r-1] using segment tree
            prev = st.check(l, r - 1)

            # Tail gap from r to x (if we consider region up to x)
            tail = x - r

            # Maximum gap that can be used before x
            mx = max(prev, tail)

            # Check if this maximum gap is at least sz
            res.append(mx >= sz)

    return res


# ----------------------------------------------------------------
# Test cases with inputs inside code (no `if __name__ == "__main__"`)
# ----------------------------------------------------------------
queries1 = [
    [1, 5],   # add obstacle at 5
    [2, 7, 3],# check if gap >= 3 before 7
    [1, 10],  # add obstacle at 10
    [2, 15, 5],# check if gap >= 5 before 15
]

print("queries1 =", queries1)
print("getResults =", getResults(queries1))

queries2 = [
    [1, 3],
    [1, 7],
    [2, 5, 2],
    [2, 9, 5],
]

print("\nqueries2 =", queries2)
print("getResults =", getResults(queries2))

queries3 = [
    [2, 10, 5],   # check before any obstacles (only 0..MX)
    [1, 5],
    [2, 3, 3],
]

print("\nqueries3 =", queries3)
print("getResults =", getResults(queries3))