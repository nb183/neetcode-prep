class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1 * stone for stone in stones]

        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = -1 * heapq.heappop(maxHeap)
            x = -1 * heapq.heappop(maxHeap)

            if x < y:
                new_weight = y - x
                heapq.heappush(maxHeap, -1 * new_weight)
        
        return -1 * maxHeap[-1] if len(maxHeap) else 0
        

        