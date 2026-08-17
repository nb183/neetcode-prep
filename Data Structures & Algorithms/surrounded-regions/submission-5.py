class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])

        def dfs(x, y):
            if x < 0 or y < 0 or x == n or y == m or board[x][y] != "O":
                return
            board[x][y] = "*"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i in (0, n-1) or j in (0, m-1)):
                    dfs(i, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "*":
                    board[i][j] = "O"