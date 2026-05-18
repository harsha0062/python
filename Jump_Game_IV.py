from collections import deque, defaultdict
from typing import List

def minJumps(arr: List[int]) -> int:
    """
    Minimum jumps to reach last index of array.
    At index i, you may jump to:
        - i + 1
        - i - 1
        - j such that arr[i] == arr[j] and i != j

    Uses BFS layered by number of steps, with a map from value → list of indices
    to quickly jump to all same‑valued indices and then clear that list to avoid
    revisiting them in later steps.
    """
    n = len(arr)
    if n <= 1:
        return 0

    # Build map from value to all indices where it appears
    indicesOfValues = defaultdict(list)
    for i in range(n):
        indicesOfValues[arr[i]].append(i)

    # BFS setup
    visited = [False] * n
    visited[0] = True
    q = deque([0])  # store indices (not steps)
    step = 0

    while q:
        # Process current BFS level (same step count)
        for _ in range(len(q)):
            i = q.popleft()

            # If we reached the last index, return current step count
            if i == n - 1:
                return step

            # Next possible indices:
            # - all indices with the same value as arr[i]
            # - i - 1 and i + 1
            nex = indicesOfValues[arr[i]] + [i - 1, i + 1]

            for j in nex:
                if 0 <= j < n and not visited[j]:
                    visited[j] = True
                    q.append(j)

            # Clear the list of indices for this value to avoid redundant BFS branches
            indicesOfValues[arr[i]].clear()

        step += 1  # move to next level / +1 jump

    return step


# Test cases with inputs written directly in code
arr1 = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
print("arr1 =", arr1)
print("minJumps(arr1) =", minJumps(arr1.copy()))  # Expected: 3

arr2 = [7]
print("arr2 =", arr2)
print("minJumps(arr2) =", minJumps(arr2.copy()))  # 0

arr3 = [7, 6, 9, 6, 9, 6, 9, 7]
print("arr3 =", arr3)
print("minJumps(arr3) =", minJumps(arr3.copy()))  # 1

arr4 = [6, 1, 9]
print("arr4 =", arr4)
print("minJumps(arr4) =", minJumps(arr4.copy()))  # 2