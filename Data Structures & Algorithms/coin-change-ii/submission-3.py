class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        
        for i in range(1, n + 1):
            for j in range (1, 1 + amount):
                dp[i][j] += dp[i - 1][j]

                if j - coins[i - 1] >= 0:
                    dp[i][j] += dp[i][j - coins[i - 1]]

        return dp[n][amount]



        # cache = {}
        # def dfs(i, rem_amount):
        #     if rem_amount == 0:
        #         return 1
        #     if i == n or rem_amount < 0:
        #         return 0
            
        #     if (i, rem_amount) in cache:
        #         return cache[(i, rem_amount)]
            
        #     # skip i:
        #     skip = dfs(i + 1, rem_amount)

        #     #include i
        #     include = dfs(i, rem_amount - coins[i])
            
        #     cache[(i, rem_amount)] = skip + include 

        #     return cache[(i, rem_amount)]

        # return dfs(0, amount)
  
        