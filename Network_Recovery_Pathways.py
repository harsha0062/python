from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        """
        Return the maximum edge weight threshold such that there exists a path
        from node 0 to node n-1:
        - using only online nodes
        - using only edges with weight >= threshold
        - with total path cost <= k
        """

        n = len(online)
        adj = defaultdict(list)

        # Build graph only with online endpoints
        all_weights = []
        for a, b, w in edges:
            if not online[a] or not online[b]:
                continue
            adj[a].append((w, b))
            all_weights.append(w)

        # If no valid edges exist, no path is possible
        if not all_weights:
            return -1

        def check(limit: int) -> bool:
            """
            Dijkstra-style feasibility check:
            Can we reach n-1 from 0 using only edges >= limit
            and total cost <= k?
            """
            h = [(0, 0)]  # (cost_so_far, node)
            dist = [k + 1] * n
            dist[0] = 0

            while h:
                w, node = heapq.heappop(h)

                if w > dist[node]:
                    continue

                if node == n - 1:
                    return True

                for nw, nei in adj[node]:
                    if nw < limit:
                        continue

                    acc = w + nw
                    if acc < dist[nei] and acc <= k:
                        dist[nei] = acc
                        heapq.heappush(h, (acc, nei))

            return False

        l = min(all_weights)
        r = max(all_weights)
        res = -1

        while l <= r:
            mid = l + (r - l) // 2

            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res