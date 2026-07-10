from typing import List
import bisect

def pathExistenceQueries(n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
    # Convert nums into (value, original_index) pairs and sort by value
    nums = [(v, i) for i, v in enumerate(nums)]
    nums.sort()

    # Map original index -> sorted position
    ntoi = {}
    for i, (v, node) in enumerate(nums):
        ntoi[node] = i

    # maxjumps[i] = farthest sorted index reachable from i in one jump
    maxjumps = [0] * n
    for i, (v, node) in enumerate(nums):
        nxt = bisect.bisect_left(nums, (v + maxDiff, float("inf"))) - 1
        maxjumps[i] = nxt

    # Binary lifting table
    LOG = n.bit_length()
    up = [maxjumps]
    for _ in range(1, LOG):
        last = up[-1]
        up.append([last[last[i]] for i in range(n)])

    res = []
    for a, b in queries:
        # Convert original indices to sorted positions
        a = ntoi[a]
        b = ntoi[b]

        # Same node
        if a == b:
            res.append(0)
            continue

        # Ensure a < b in sorted order
        if a > b:
            a, b = b, a

        curr, jumps = a, 0

        # Jump as far as possible without passing b
        for k in range(LOG - 1, -1, -1):
            if up[k][curr] < b:
                curr = up[k][curr]
                jumps += 2 ** k

        # Final step if reachable
        if maxjumps[curr] >= b:
            res.append(jumps + 1)
        else:
            res.append(-1)

    return res


# Input inside the code
n = 5
nums = [1, 3, 6, 7, 10]
maxDiff = 2
queries = [[0, 1], [1, 2], [2, 4], [0, 4], [3, 3]]

print(pathExistenceQueries(n, nums, maxDiff, queries))