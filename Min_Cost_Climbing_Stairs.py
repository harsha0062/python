from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    # Add a zero-cost step at the top of the staircase
    cost.append(0)

    # Calculate the minimum cost from each step to the top
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])

    # You can start from step 0 or step 1
    return min(cost[0], cost[1])


# Input inside the code
cost = [10, 15, 20]

print(minCostClimbingStairs(cost))