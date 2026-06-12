from typing import List
from collections import defaultdict, deque
from functools import cache

# ----------------------------------------------------------------
# assignEdgeWeights(edges, queries):
#
# Problem idea (based on the code and similar LeetCode problems):
#   - Given a tree (undirected, n nodes, n-1 edges), root it at node 1.
#   - For each query (a, b), consider the unique path between a and b.
#   - The number of ways to assign edge weights (0 or 1) on this path
#     under certain constraints is 2^(distance - 1) % MOD, where distance
#     is the number of edges on the path between a and b.
#   - If distance == 0 (a == b), the answer is 0.
#
# Algorithm:
#   1. Build adjacency list from edges.
#   2. BFS from node 1 to compute:
#        - depth (level) of each node
#        - parent of each node
#   3. Implement LCA (lowest common ancestor) by moving the deeper node up
#      until both nodes are at the same depth, then move both up until they meet.
#   4. For each query (a, b):
#        - Compute l = LCA(a, b).
#        - distance = (depth[a] - depth[l]) + (depth[b] - depth[l]).
#        - answer = 0 if distance == 0, else 2^(distance - 1) % MOD.
#   5. Return list of answers.
# ----------------------------------------------------------------
def assignEdgeWeights(edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    """
    For each query (a, b), compute the number of ways to assign edge weights
    on the path between a and b in a tree, based on the path length.

    Returns:
        List of integers: for each query, the number of ways modulo 10^9 + 7.
    """
    MOD = 10**9 + 7

    # 1. Build adjacency list
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    # 2. BFS from node 1 to compute depth and parent for each node
    mp = {}  # mp[node] = [depth, parent]
    q = deque()
    q.append((1, 0, -1))  # (node, depth, parent)

    while q:
        node, lvl, par = q.popleft()
        mp[node] = [lvl, par]
        for nei in adj[node]:
            if nei != par:
                q.append((nei, lvl + 1, node))

    # 3. LCA function using depth and parent
    @cache
    def lca(a: int, b: int) -> int:
        """
        Find the lowest common ancestor of a and b.
        Move the deeper node up until both are at the same depth,
        then move both up until they meet.
        """
        # Bring a up if it's deeper
        while mp[a][0] > mp[b][0]:
            a = mp[a][1]
        # Bring b up if it's deeper
        while mp[a][0] < mp[b][0]:
            b = mp[b][1]
        # Move both up until they meet
        while a != b:
            a = mp[a][1]
            b = mp[b][1]
        return a

    # 4. Process each query
    res = []
    for a, b in queries:
        l = lca(a, b)
        depth_a, depth_b, depth_l = mp[a][0], mp[b][0], mp[l][0]

        # Distance = number of edges on the path between a and b
        dist = (depth_a - depth_l) + (depth_b - depth_l)

        if dist == 0:
            res.append(0)
        else:
            res.append(pow(2, dist - 1, MOD))

    return res


# ----------------------------------------------------------------
# Test cases with inputs inside code (no `if __name__ == "__main__"`)
# ----------------------------------------------------------------
# Example 1: Tree 1-2-3-4, queries on paths
edges1 = [[1, 2], [2, 3], [3, 4]]
queries1 = [[1, 4], [2, 3], [1, 1]]
print("edges1 =", edges1)
print("queries1 =", queries1)
print("assignEdgeWeights =", assignEdgeWeights(edges1, queries1))
# Tree: 1-2-3-4, root at 1
# Query (1,4): path 1-2-3-4, length=3 → 2^(3-1)=4
# Query (2,3): path 2-3, length=1 → 2^(1-1)=1
# Query (1,1): length=0 → 0

# Example 2: Star tree 1 connected to 2,3,4
edges2 = [[1, 2], [1, 3], [1, 4]]
queries2 = [[2, 3], [2, 4], [3, 4]]
print("\nedges2 =", edges2)
print("queries2 =", queries2)
print("assignEdgeWeights =", assignEdgeWeights(edges2, queries2))
# Star: 1 is center, all leaves at depth 1
# (2,3): path 2-1-3, length=2 → 2^(2-1)=2
# (2,4): path 2-1-4, length=2 → 2
# (3,4): path 3-1-4, length=2 → 2

# Example 3: Larger tree
edges3 = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]]
queries3 = [[4, 5], [4, 6], [5, 6]]
print("\nedges3 =", edges3)
print("queries3 =", queries3)
print("assignEdgeWeights =", assignEdgeWeights(edges3, queries3))
# Tree:
#   1
#  / \
# 2   3
# |\   \
# 4 5   6
# (4,5): path 4-2-5, length=2 → 2
# (4,6): path 4-2-1-3-6, length=4 → 2^(4-1)=8
# (5,6): path 5-2-1-3-6, length=4 → 8

# Detailed BFS and LCA trace for edges1
print("\nBFS and LCA trace for edges1 = [[1,2],[2,3],[3,4]]:")
edges = [[1, 2], [2, 3], [3, 4]]
adj = defaultdict(list)
for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)

mp = {}
q = deque([(1, 0, -1)])
while q:
    node, lvl, par = q.popleft()
    mp[node] = [lvl, par]
    print(f"node={node}, depth={lvl}, parent={par}")
    for nei in adj[node]:
        if nei != par:
            q.append((nei, lvl + 1, node))

print("\nmp (depth, parent):", mp)

queries = [[1, 4], [2, 3]]
for a, b in queries:
    # Compute LCA
    x, y = a, b
    while mp[x][0] > mp[y][0]:
        x = mp[x][1]
    while mp[x][0] < mp[y][0]:
        y = mp[y][1]
    while x != y:
        x = mp[x][1]
        y = mp[y][1]
    l = x
    dist = (mp[a][0] - mp[l][0]) + (mp[b][0] - mp[l][0])
    ans = 0 if dist == 0 else pow(2, dist - 1, 10**9 + 7)
    print(f"Query ({a},{b}): LCA={l}, distance={dist}, answer={ans}")