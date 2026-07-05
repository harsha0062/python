from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Return the maximum profit from one buy and one sell.

        Idea:
        - l tracks the best day to buy so far.
        - r scans forward as the sell day.
        - If prices[r] is lower, move l to r.
        - Otherwise, update max profit.
        """
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP


# Test cases inside the code
sol = Solution()

prices1 = [7,1,5,3,6,4]
print(sol.maxProfit(prices1))  # 5

prices2 = [7,6,4,3,1]
print(sol.maxProfit(prices2))  # 0

prices3 = [1,2,3,4,5]
print(sol.maxProfit(prices3))  # 4