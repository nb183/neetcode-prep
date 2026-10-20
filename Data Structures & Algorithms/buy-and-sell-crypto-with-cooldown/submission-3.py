class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def solve(i, turn): # 0 for buy, 1 for sale
            if i >= len(prices):
                return 0
            
            if (i, turn) in dp:
                return dp[(i, turn)]

            curr = 0

            if turn == 0:
                curr = max(solve(i + 1, 1) - prices[i], solve(i + 1, 0))
            
            else:
                curr = max(solve(i + 2, 0) + prices[i], solve(i + 1, 1))
            
            dp[(i, turn)] = curr
            return curr


        return solve(0, 0)
            

