from typing import List

def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    # Store whether each node is safe or unsafe
    safe = {}

    def dfs(i):
        # Return the previously calculated result
        if i in safe:
            return safe[i]

        # Mark the node as unsafe before exploring its neighbors.
        # This also detects cycles during recursion.
        safe[i] = False

        # Check every neighboring node
        for nei in graph[i]:
            # If any neighbor is unsafe, the current node is unsafe
            if not dfs(nei):
                return False

        # All neighbors are safe, so the current node is safe
        safe[i] = True
        return True

    # Store all safe nodes
    res = []

    # Check every node in the graph
    for i in range(len(graph)):
        if dfs(i):
            res.append(i)

    return res


# Input inside the code
graph = [
    [1, 2],
    [2, 3],
    [5],
    [0],
    [5],
    [],
    []
]

print(eventualSafeNodes(graph))