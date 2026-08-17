class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            count = 0
            stack = [(i, j)]
            while stack:
                row, col = stack.pop()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for d in directions:
                    nr, nc = row + d[0], col + d[1]
                    if (
                        nr >= 0
                        and nr < r
                        and nc >= 0
                        and nc < c
                        and grid[nr][nc]
                        and (nr, nc) not in visited
                    ):
                        stack.append((nr, nc))
                if (row, col) not in visited:
                    count += 1
                    visited.add((row, col))
  
            return count

        maximum = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] and (i, j) not in visited:
                    maximum = max(maximum, dfs(i, j))
                    
        return maximum