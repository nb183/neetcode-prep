class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        queue1, queue2 = deque(), deque()

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 :
                    queue1.append((i, j))
                    pacific.add((i, j))
                
                if i == m - 1 or j == n - 1:
                    queue2.append((i, j))
                    atlantic.add((i, j))

            
        while queue1:
            i, j = queue1.popleft()
            for x, y in directions:
                ni, nj = i + x, j + y
                if 0 <= ni < m and 0 <= nj < n and heights[ni][nj] >= heights[i][j] and (ni, nj) not in pacific:
                    queue1.append((ni, nj))
                    pacific.add((ni, nj))

        while queue2:
            i, j = queue2.popleft()
            for x, y in directions:
                ni, nj = i + x, j + y

                if 0 <= ni < m and 0 <= nj < n and heights[ni][nj] >= heights[i][j] and (ni, nj) not in atlantic:
                    queue2.append((ni, nj))
                    atlantic.add((ni, nj))

        ans = []
        for x, y in pacific:
            if (x, y) in atlantic:
                ans.append([x, y])

        return ans
            
        


        


        