class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def solve(profit, i, turn): # 0 for buy, 1 for sale
            if i >= len(prices):
                return profit
            
            if (profit, i, turn) in dp:
                return dp[(profit, i, turn)]

            curr = 0

            if turn == 0:
                curr = max(solve(profit - prices[i], i + 1, 1), solve(profit, i + 1, 0))
            
            else:
                curr = max(solve(profit + prices[i], i + 2, 0), solve(profit, i + 1, 1))
            
            dp[(profit, i, turn)] = curr
            return curr


        return solve(0, 0, 0)
            

