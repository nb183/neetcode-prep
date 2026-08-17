class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        minimum = prices[0]

        for i in range(1, len(prices)):
            if prices[i] <= minimum:
                minimum = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - minimum)
        return max_profit