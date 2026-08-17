class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        x, y = len(s), len(t) 

        if y > x: return 0

        dp = [[0]*(y+1) for _ in range(x+1)]
         
        for i in range(x+1):
            dp[i][0] = 1

        for i in range(1, x+1):
            for j in range(1, y+1):
                if s[i-1] == t[j-1]: 
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else: 
                    dp[i][j] = dp[i-1][j]

        return dp[x][y] 