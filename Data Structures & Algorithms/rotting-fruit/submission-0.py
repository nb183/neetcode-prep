class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ans = 0
        while queue and fresh > 0:
            ans += 1

            for _ in range(len(queue)):
                x, y = queue.popleft()
                for d in directions:
                    nx = x + d[0]
                    ny = y + d[1]

                    if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == 1:
                        queue.append((nx, ny))
                        grid[nx][ny] = 2
                        fresh -= 1


        if fresh == 0:
            return ans
        else:
            return -1
