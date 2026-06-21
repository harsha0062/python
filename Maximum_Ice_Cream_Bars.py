from typing import List

def maxIceCream(costs: List[int], coins: int) -> int:
    """
    Find the maximum number of ice cream bars you can buy with given coins.

    Strategy:
      - Sort the costs in non-decreasing order.
      - Buy the cheapest ice creams first until you can't afford the next one.
      - Return the count of ice creams bought.

    Algorithm:
      1. Sort `costs`.
      2. Initialize count i = 0.
      3. While i < len(costs) and coins >= costs[i]:
           - Subtract costs[i] from coins.
           - Increment i.
      4. Return i.

    This is a greedy approach: buying the cheapest first maximizes the count.
    """
    costs.sort()  # Sort costs from cheapest to expensive

    i = 0
    # Buy as many as possible, starting from the cheapest
    while i < len(costs) and coins >= costs[i]:
        coins -= costs[i]
        i += 1

    return i


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
costs1 = [1, 3, 2, 4, 1]
coins1 = 7
print("costs1 =", costs1)
print("coins1 =", coins1)
print("maxIceCream =", maxIceCream(costs1, coins1))
# Sorted: [1, 1, 2, 3, 4]
# Buy: 1 (coins=6), 1 (coins=5), 2 (coins=3), 3 (coins=0) → can't buy 4
# Count = 4

costs2 = [10, 6, 8, 7, 7, 8]
coins2 = 5
print("\ncosts2 =", costs2)
print("coins2 =", coins2)
print("maxIceCream =", maxIceCream(costs2, coins2))
# Sorted: [6, 7, 7, 8, 8, 10]
# Can't buy even the cheapest (6 > 5) → count = 0

costs3 = [1, 6, 3, 1, 2, 5]
coins3 = 10
print("\ncosts3 =", costs3)
print("coins3 =", coins3)
print("maxIceCream =", maxIceCream(costs3, coins3))
# Sorted: [1, 1, 2, 3, 5, 6]
# Buy: 1 (9), 1 (8), 2 (6), 3 (3), 5 (can't, 5 > 3)
# Count = 4

# Detailed trace for costs1, coins1
print("\nDetailed trace for costs1=[1,3,2,4,1], coins1=7:")
costs = [1, 3, 2, 4, 1]
coins = 7

costs.sort()
print("Sorted costs:", costs)

i = 0
while i < len(costs):
    if coins >= costs[i]:
        print(f"  Buy ice cream #{i+1} with cost {costs[i]}: coins {coins} → {coins - costs[i]}")
        coins -= costs[i]
        i += 1
    else:
        print(f"  Cannot buy ice cream #{i+1} with cost {costs[i]}: coins {coins} < {costs[i]}")
        break

print(f"Total ice creams bought: {i}")