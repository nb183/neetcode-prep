class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))

        visited = set()

        heap = [(0, k)]

        t = 0
        while heap:
            t1, u = heapq.heappop(heap)

            if u in visited:
                continue
            visited.add(u)
            t = t1
            for v, t2 in graph[u]:
                if v not in visited:
                    heapq.heappush(heap, (t + t2, v))
        return t if n == len(visited) else -1


