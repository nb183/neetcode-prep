class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Bruteforce -> For each "1" value in the matrix, we can expand different sized squares(1, 2, 3, <= min(m, n)) and check if all of the values in there are ones and get maximum of that. TC -> O(m * n * min(m, n)) ~ O(n^4) SC -> O(1)

        # Optimized -> recursion + memoization. For each 1 we encounter, we can check what is the largest square the item directly right, down, and diagonally to its make. Then we can take the minimum of those and expand by 1 to get the largest square that cant be made from current1. We have to memoize the results to not do redundant computation. TC -> O(N^2), space O(N^2)
        # Optimzed - bottom up dp

        # Optimal
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for i in range(m)]
        ans = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "0":
                    continue
                right = down = diag = 0
                if i + 1 < m:
                   down = dp[i + 1][j]
                if j + 1 < n:
                    right = dp[i][j + 1]
                if i + 1 < m and j + 1 < n:
                    diag =  dp[i + 1][j + 1]
                dp[i][j] = min(right, down, diag) + 1
                ans = max(ans, dp[i][j])

        # ans  = 0
        # for i in range(m):
        #     for j in range(n):
        #         ans = max(ans, dp[i][j])
        return ans * ans

                
            
        