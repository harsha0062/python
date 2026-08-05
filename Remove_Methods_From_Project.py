from typing import List
from collections import defaultdict

def remainingMethods(n: int, k: int, invocations: List[List[int]]) -> List[int]:
    # Build graph and indegree array
    adj = defaultdict(list)
    indegree = [0] * n

    for a, b in invocations:
        adj[a].append(b)
        indegree[b] += 1

    # Store all suspicious methods reachable from k
    susp = set()

    def dfs(node: int):
        # Mark this node as suspicious
        susp.add(node)

        # Visit all outgoing neighbors
        for nei in adj[node]:
            # Decrease indegree as in the original logic
            indegree[nei] -= 1

            # Recurse only if the neighbor has not been visited yet
            if nei not in susp:
                dfs(nei)

    # Start DFS from the given method k
    dfs(k)

    # If any suspicious node still has positive indegree,
    # return all methods
    for node in susp:
        if indegree[node]:
            return list(range(n))

    # Otherwise return all non-suspicious methods
    return [node for node in range(n) if node not in susp]


# Input inside the code
n = 5
k = 1
invocations = [[1, 2], [2, 3], [0, 1], [3, 4]]

print(remainingMethods(n, k, invocations))