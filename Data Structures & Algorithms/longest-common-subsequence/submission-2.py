class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        dp = [[0] * (n+1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

        # cache = {}
        # def dfs(i, j):
        #     if i == m or j == n:
        #         return 0
            
        #     if (i, j) in cache:
        #         return cache[(i, j)]

        #     if text1[i] == text2[j]:
        #         cache[(i, j)] = 1 + dfs(i + 1, j + 1)
        #     else:
        #         cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))

        #     return cache[(i, j)]
        # return dfs(0, 0)
        