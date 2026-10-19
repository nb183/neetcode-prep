class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_path = [[-1] * n for _ in range(m)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y):
            max_path[x][y] = 1
            for r, c in directions:
                nx, ny = r + x, c + y 
                if nx >= 0 and nx < m and ny >= 0 and ny < n:
                    if matrix[nx][ny] > matrix[x][y]:
                        if max_path[nx][ny] == -1: 
                            dfs(nx, ny)
                        max_path[x][y] = max(max_path[x][y], max_path[nx][ny] + 1)

        maxm = -1
        for i in range(m):
            for j in range(n):
                if max_path[i][j] == -1:
                    dfs(i, j)
                maxm = max(maxm, max_path[i][j])

        return maxm