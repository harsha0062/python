from functools import cache
from typing import List

# Given input inside the code
price = [3, 2, 6, 5, 0, 3]
k = 2

def maximumProfit(price: List[int], k: int) -> int:
    n = len(price)

    # dfs(i, j, state)
    # i     -> current day index
    # j     -> remaining transactions
    # state -> 0 = no stock
    #          1 = holding stock (bought)
    #          2 = sold stock
    @cache
    def dfs(i, j, state):
        # If no transactions left, profit is 0
        if j == 0:
            return 0

        # Base case: first day
        if i == 0:
            if state == 0:
                return 0                 # do nothing
            elif state == 1:
                return -price[0]         # buy on day 0
            else:
                return price[0]          # sell on day 0

        p = price[i]

        # State 0: no stock
        if state == 0:
            res = max(
                dfs(i-1, j, 0),           # stay idle
                dfs(i-1, j, 1) + p,       # sell stock
                dfs(i-1, j, 2) - p        # buy again
            )

        # State 1: holding stock
        elif state == 1:
            res = max(
                dfs(i-1, j, 1),           # keep holding
                dfs(i-1, j-1, 0) - p      # buy stock
            )

        # State 2: sold stock
        else:
            res = max(
                dfs(i-1, j, 2),           # stay sold
                dfs(i-1, j-1, 0) + p      # sell stock
            )

        return res

    # Final answer: last day, k transactions, no stock
    ans = dfs(n-1, k, 0)

    # Clear cache
    dfs.cache_clear()
    return ans


# Call the function and print output
result = maximumProfit(price, k)
print("Maximum Profit:", result)
