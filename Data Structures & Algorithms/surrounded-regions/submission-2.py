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

        def dfs2(x, y, sym1, sym2):
            seen.add((x,y))
            if board[x][y] == sym1:
                board[x][y] = sym2
            for d1, d2 in directions:
                nx = x + d1
                ny = y + d2
                if 0 <=nx<n and 0<=ny<m and (nx, ny) not in seen:
                    dfs2(nx, ny, sym1, sym2)
        for i in range(n):
            dfs(i, 0)

        for i in range(n):
            seen.clear()
            dfs(n-i-1, m-1)
        for i in range(m):
            seen.clear()
            dfs(0, i)
        for i in range(m):
            seen.clear()
            dfs(n-1, m-i-1)
        print(board)
        seen.clear()
        dfs2(0, 0, "O", "X")
        seen.clear()
        dfs2(0, 0, "*", "O")


            
            




        