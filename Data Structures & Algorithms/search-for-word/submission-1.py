class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	
        m = len(board)
        n = len(board[0])

        def dfs(x, y, pos):
            if board[x][y] != word[pos]:
                return False
            if pos == len(word) - 1:
                return True
            curr = board[x][y]
            board[x][y] = "*"
            for i, j in directions:
                nx, ny = x + i, y + j
                if nx < m and nx >= 0 and ny < n and ny >= 0 and board[nx][ny] != "*":
                   if dfs(nx, ny, pos + 1):
                        return True
            board[x][y] = curr
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


 
