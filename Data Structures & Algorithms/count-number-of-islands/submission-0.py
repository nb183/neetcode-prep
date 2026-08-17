class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        ans = 0
        visited = set()

        def dfs(i, j):
            stack = [(i, j)]
            while stack:
                row, col = stack.pop()
                directions = [(1,0),(-1, 0), (0, 1), (0, -1)]

                for d in directions:
                    nr, nc = row + d[0], col + d[1]
                    if nr >= 0 and nr < r and nc >=0 and nc < c and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        stack.append((nr, nc))
                visited.add((row, col))

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    ans += 1
        return ans