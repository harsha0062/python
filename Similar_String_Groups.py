from typing import List

def numSimilarGroups(strs: List[str]) -> int:
    # Store whether each string has already been visited
    n = len(strs)
    done = [False] * n

    def go(index):
        # Compare the current string with every unvisited string
        for i in range(n):
            if not done[i]:
                delta = 0

                # Count the number of different characters
                for a, b in zip(strs[index], strs[i]):
                    if a != b:
                        delta += 1

                    # Similar strings can differ in at most two positions
                    if delta > 2:
                        break

                # This else belongs to the for loop.
                # It executes only when the loop was not stopped by break.
                else:
                    done[i] = True
                    go(i)

    # Count the number of connected groups
    count = 0

    for i in range(n):
        if not done[i]:
            count += 1
            done[i] = True
            go(i)

    return count


# Input inside the code
strs = ["tars", "rats", "arts", "star"]

print(numSimilarGroups(strs))