class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((dist, j))
                graph[j].append((dist, i))

        visited = set()
        min_cost = 0
        heap = [(0, 0)]

        while len(visited) < n:
            d, point = heapq.heappop(heap)

            if point in visited:
                continue

            visited.add(point)
            min_cost += d

            for neigh in graph[point]:
                if neigh[1] not in visited:
                    heapq.heappush(heap, neigh)

        return min_cost