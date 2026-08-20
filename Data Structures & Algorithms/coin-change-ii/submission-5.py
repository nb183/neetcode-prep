class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for i in range(n):
            next_dp = [0] * (amount + 1)
            for j in range (1 + amount):
                next_dp[j] = dp[j]

                if j - coins[i] >= 0:
                    next_dp[j] += next_dp[j - coins[i]]
            dp = next_dp
        return dp[amount]


        