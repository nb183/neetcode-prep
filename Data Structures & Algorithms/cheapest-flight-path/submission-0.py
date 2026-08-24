class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman Ford -> O(V * E) time
        # Since we have at most k stops, we can run a modified bellman ford relaxing the edges
        # k + 1 times as k stops mean k + 2 nodes with src and destination edges

        INF = float("inf")
        dist = [INF] * n
        dist[src] = 0

        for _ in range(k + 1):
            prev_dist = dist[:]
            for u, v, w in flights:
                if prev_dist[u] != INF and prev_dist[u] + w < dist[v]:
                    dist[v] = prev_dist[u] + w

        return dist[dst] if dist[dst] != INF else -1
        