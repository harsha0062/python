from typing import List

def maxProfit(prices: List[int], strategy: List[int], k: int) -> int:
    """
    prices   : list of stock prices
    strategy : list indicating strategy (+1 or -1)
    k        : window size
    """

    n = len(prices)

    # profitsum[i] = total profit till index i-1
    profitsum = [0] * (n + 1)

    # pricesum[i] = sum of prices till index i-1
    pricesum = [0] * (n + 1)

    # Build prefix sums
    for i in range(n):
        profitsum[i + 1] = profitsum[i] + prices[i] * strategy[i]
        pricesum[i + 1] = pricesum[i] + prices[i]

    # Initial result: profit without any change
    res = profitsum[n]

    # Sliding window from k-1 to n-1
    for i in range(k - 1, n):

        # Profit before the k-length window
        left = profitsum[i - k + 1]

        # Profit after the k-length window
        right = profitsum[n] - profitsum[i + 1]

        # Profit gained by modifying strategy in half window
        change = pricesum[i + 1] - pricesum[i - k // 2 + 1]

        # Update maximum profit
        res = max(res, left + right + change)

    return res


# ---------------- INPUT GIVEN INSIDE THE CODE ----------------

prices = [3, 2, 6, 5, 0, 3]
strategy = [1, -1, 1, -1, 1, -1]
k = 4

# Function call
result = maxProfit(prices, strategy, k)

# Output
print("Maximum Profit:", result)
