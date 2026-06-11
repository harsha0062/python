from typing import List
from collections import defaultdict, deque

# ----------------------------------------------------------------
# assignEdgeWeights(edges):
#
# Problem idea (based on the code and similar LeetCode problems):
#   - Given a tree (n nodes, n-1 edges), assign each edge a weight of either 0 or 1.
#   - Count the number of ways to assign weights such that the maximum distance
#     between any two nodes is minimized (or some related condition).
#   - The given solution:
#       * Builds an adjacency list.
#       * BFS from node 1 to compute the maximum depth (distance from root) in the tree.
#       * Returns 2^(max_depth - 1) mod (10^9 + 7).
#
# Interpretation:
#   - mxlvl is the maximum level (depth) of any node when rooted at 1.
#   - The number of valid assignments is related to the height of the tree.
#   - Result = 2^(mxlvl - 1) % MOD.
#
# This matches problems like "Number of Ways to Assign Edge Weights I/II".
# ----------------------------------------------------------------
def assignEdgeWeights(edges: List[List[int]]) -> int:
    """
    Compute the number of ways to assign edge weights (0 or 1) in a tree
    under certain constraints, based on the tree's height.

    Algorithm:
      1. Build adjacency list from edges.
      2. BFS from node 1 to compute the maximum depth (mxlvl) of the tree.
      3. Return 2^(mxlvl - 1) % MOD.
    """
    MOD = 10**9 + 7
    adj = defaultdict(list)

    # Build adjacency list
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    # BFS from node 1 to find maximum depth
    q = deque([(1, 0, -1)])  # (node, level, parent)
    mxlvl = 0

    while q:
        node, lvl, par = q.popleft()
        if lvl > mxlvl:
            mxlvl = lvl

        for nei in adj[node]:
            if nei != par:
                q.append((nei, lvl + 1, node))

    # Result is 2^(mxlvl - 1) % MOD
    # If mxlvl == 0, this would be 2^(-1), but in practice for a single node tree,
    # edges is empty and mxlvl=0; the intended formula is for trees with at least one edge.
    if mxlvl == 0:
        return 0
    return pow(2, mxlvl - 1, MOD)


# ----------------------------------------------------------------
# Test cases with inputs inside code (no `if __name__ == "__main__"`)
# ----------------------------------------------------------------
# Example 1: Simple line 1-2-3
edges1 = [[1, 2], [2, 3]]
print("edges1 =", edges1)
print("assignEdgeWeights =", assignEdgeWeights(edges1))
# Tree: 1-2-3, root at 1, max depth = 2 → 2^(2-1) = 2

# Example 2: Star 1 connected to 2,3,4
edges2 = [[1, 2], [1, 3], [1, 4]]
print("\nedges2 =", edges2)
print("assignEdgeWeights =", assignEdgeWeights(edges2))
# Tree: 1 is center, all leaves at depth 1 → max depth = 1 → 2^(1-1) = 1

# Example 3: 1-2, 2-3, 3-4 (line of 4)
edges3 = [[1, 2], [2, 3], [3, 4]]
print("\nedges3 =", edges3)
print("assignEdgeWeights =", assignEdgeWeights(edges3))
# Depth from 1: 1→0, 2→1, 3→2, 4→3 → max depth = 3 → 2^(3-1) = 4

# Example 4: Single node (no edges)
edges4 = []
print("\nedges4 =", edges4)
print("assignEdgeWeights =", assignEdgeWeights(edges4))
# mxlvl = 0 → returns 0 by special case

# BFS trace for edges1 = [[1,2],[2,3]]
print("\nBFS trace for edges1 = [[1,2],[2,3]]:")
edges = [[1, 2], [2, 3]]
adj = defaultdict(list)
for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)

q = deque([(1, 0, -1)])
mxlvl = 0
while q:
    node, lvl, par = q.popleft()
    print(f"node={node}, level={lvl}, parent={par}")
    if lvl > mxlvl:
        mxlvl = lvl
    for nei in adj[node]:
        if nei != par:
            q.append((nei, lvl + 1, node))

print("maxlvl =", mxlvl)
print("result = 2^(maxlvl - 1) =", pow(2, mxlvl - 1, 10**9 + 7))