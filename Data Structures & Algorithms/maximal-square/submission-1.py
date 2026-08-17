class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Bruteforce -> For each "1" value in the matrix, we can expand different sized squares(1, 2, 3, <= min(m, n)) and check if all of the values in there are ones and get maximum of that. TC -> O(m * n * min(m, n)) ~ O(n^4) SC -> O(1)

        # Optimal
        m = len(matrix)
        n = len(matrix[0])

        dp = [[-1] * n for i in range(m)]

        def solve(i, j):
            if matrix[i][j] == "0":
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            right, down, diag = 0, 0, 0

            if j + 1 < n:
                right = solve(i, j + 1)
            if i + 1 < m:
                down = solve(i + 1, j)
            if (i + 1 < m and j + 1 < n):
                diag = solve(i + 1, j + 1)
            
            dp[i][j] = min(right, down, diag) + 1
            return dp[i][j]
        
        
        ans = 0
        for i in range(m):
            for j in range(n):
                res =  solve(i, j)
                print(i, j, res)
                ans = max(ans, res)
        return ans * ans
                
            
        