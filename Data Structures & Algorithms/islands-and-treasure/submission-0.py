class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Bruteforce -> O(N * M)^2 time, O(N * M) space
        # We can do a bfs from each land cell, and find the closest treasure chest.

        # Bruteforce 2 -> O(N * M) ^ 2 time, O(N * M) space
        # We can run BFS from each treasure chest updating the values in the land cells. In doing this,
        # we can check if then curret distance is less that the previous distance and only update the cell and
        # add that path to the queue. Otherwise, we leave it unchaged. 

        # Optimal -> O(N * M) time, O(N * M) space
        # We can do something like a multisource BFS. Similar to bruteforce 2, we carry out BFS from each 
        # treasure chest. For, intially, we enqueue all the treasure chest cell and then carry out BFs
        # from their level by level, updating the distances if it is a land cell and not visited (non inf)

        R, C = len(grid), len(grid[0])
        q = deque()

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for x, y in directions:
                ni = i + x
                nj = j + y

                if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] != -1 and grid[ni][nj] > 100000:
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni, nj))
        

        