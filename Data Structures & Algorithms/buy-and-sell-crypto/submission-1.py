class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        minimum = prices[0]

        for item in prices:
            minimum = min(item, minimum)
            max_profit = max(max_profit, item - minimum)
        return max_profit