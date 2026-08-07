from typing import List
from collections import defaultdict

def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
    # Get the length of the string
    n = len(s)

    # Initially, every index is its own parent
    parent = list(range(n))

    def find(a):
        # Find the root parent of index a
        # Path compression makes future searches faster
        if parent[a] != a:
            parent[a] = find(parent[a])

        return parent[a]

    def union(a, b):
        # Join the groups containing indices a and b
        parent[find(a)] = find(b)

    # Connect all indices that can be swapped
    for a, b in pairs:
        union(a, b)

    # Store indices and characters belonging to each group
    groups_i = defaultdict(list)
    groups_ch = defaultdict(list)

    for i in range(n):
        group = find(i)
        groups_i[group].append(i)
        groups_ch[group].append(s[i])

    # Store the final smallest string
    res = [""] * n

    # Sort indices and characters within each connected group
    for g in groups_i.keys():
        idx = sorted(groups_i[g])
        ch = sorted(groups_ch[g])

        # Assign the smallest characters to the smallest indices
        for i, c in zip(idx, ch):
            res[i] = c

    return "".join(res)


# Input inside the code
s = "dcab"
pairs = [[0, 3], [1, 2]]

print(smallestStringWithSwaps(s, pairs))