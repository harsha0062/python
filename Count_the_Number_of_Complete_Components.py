from typing import List
from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list using sets for fast edge lookup
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        # DFS to collect all nodes in one connected component
        def dfs(node):
            seen.add(node)
            component.append(node)
            for nei in adj[node]:
                if nei not in seen:
                    dfs(nei)

        res = 0
        seen = set()

        # Visit every node; each DFS finds one connected component
        for node in range(n):
            if node not in seen:
                component = []
                dfs(node)

                c = len(component)
                valid = True

                # A complete component of size c must have exactly c*(c-1)/2 edges
                # Here we verify every pair of nodes is connected
                for i in range(c):
                    for j in range(i + 1, c):
                        if component[i] not in adj[component[j]]:
                            valid = False
                            break
                    if not valid:
                        break

                if valid:
                    res += 1

        return res


# Input inside the code
n = 6
edges = [[0, 1], [0, 2], [1, 2], [3, 4]]

sol = Solution()
print(sol.countCompleteComponents(n, edges))