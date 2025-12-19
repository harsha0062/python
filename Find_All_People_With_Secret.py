from collections import defaultdict
from typing import List

# Your original function (NOT changed)
def findAllPeople(n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    # Set to store all people who know the secret
    # Initially, person 0 and firstPerson know the secret
    secrets = set([0, firstPerson])

    # Dictionary to map each time t -> adjacency list (graph) of meetings at that time
    time_map = {}

    # Build time-wise graphs
    for src, dst, t in meetings:
        if t not in time_map:
            # For each new time, create a new adjacency list using defaultdict(list)
            time_map[t] = defaultdict(list)
        # Since each meeting is between two people, add edges both ways (undirected graph)
        time_map[t][src].append(dst)
        time_map[t][dst].append(src)

    # Depth-First Search to spread the secret in the graph for a given time
    def dfs(src, adj):
        # If this node was already visited in the current time component, skip
        if src in visit:
            return
        # Mark current node visited in this time's traversal
        visit.add(src)
        # This person now knows the secret
        secrets.add(src)
        # Visit all neighbors connected in this time graph
        for nei in adj[src]:
            dfs(nei, adj)

    # Process each time in increasing order
    for t in sorted(time_map.keys()):
        # New visited set for this particular time component
        visit = set()
        # For every person who has a meeting at time t
        for src in time_map[t]:
            # If this person already knows the secret, explore their component
            if src in secrets:
                dfs(src, time_map[t])

    # Return all people who know the secret as a list
    return list(secrets)


# -------------------------------
# Example input directly in code
# -------------------------------

# Number of people
n = 6

# Meetings: [person1, person2, time]
meetings = [
    [1, 2, 5],
    [2, 3, 8],
    [1, 5, 10],
    [0, 4, 2],
    [4, 1, 3]
]

# The first person (besides 0) who knows the secret initially
firstPerson = 1

# Call the function with the above input
result = findAllPeople(n, meetings, firstPerson)

# Print the result
print("People who know the secret:", result)
