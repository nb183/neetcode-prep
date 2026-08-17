class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        n, m = len(board), len(board[0])
        seen = set()

        def dfs(x, y):
            seen.add((x,y))
            print(x, y, "here")
            if board[x][y] == "X":
                return
            if board[x][y] == "O":
                board[x][y] = "*"
            for d1, d2 in directions:
                nx = x + d1
                ny = y + d2
                if 0 <=nx<n and 0<=ny<m and board[nx][ny] == "O" and (nx,ny) not in seen:
                    dfs(nx, ny)
        for i in range(n):
            dfs(i, 0)
        for i in range(n):
            dfs(n-i-1, m-1)
        for i in range(m):
            dfs(0, i)
        for i in range(m):
            dfs(n-1, m-i-1)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "*":
                    board[i][j] = "O"