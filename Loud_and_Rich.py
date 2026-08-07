from typing import List

def loudAndRich(richer: List[List[int]], quiet: List[int]) -> List[int]:
    def dfs(graph, source, quietness, output):
        # Assume the current person is the quietest initially
        least_quiet = source

        # Check every person who is richer than the current person
        for neighbor in graph[source]:
            # Calculate the answer for the neighbor if not calculated yet
            if output[neighbor] is None:
                dfs(graph, neighbor, quietness, output)

            # Select the quieter person between the current best
            # and the best person found through the neighbor
            least_quiet = min(
                least_quiet,
                output[neighbor],
                key=lambda x: quietness[x]
            )

        # Store the quietest richer-or-equal person for this source
        output[source] = least_quiet

    # Number of people
    n = len(quiet)

    # graph[i] contains people richer than person i
    graph = [set() for i in range(n)]

    # Build the graph from richer relationships
    for relation in richer:
        richer_person, poorer_person = relation
        graph[poorer_person].add(richer_person)

    # Store the index of the quietest person for each person
    output = [None for _ in range(n)]

    # Run DFS for every person
    for person in range(n):
        if output[person] is None:
            dfs(graph, person, quiet, output)

    return output


# Input inside the code
richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
quiet = [3, 2, 5, 4, 6, 1, 7, 0]

print(loudAndRich(richer, quiet))