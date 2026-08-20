class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            dist = (points[i][0]**2 + points[i][1]**2)
            heapq.heappush(heap, (-dist, i ))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []

        for _, i in heap:
            ans.append(points[i])
        
        return ans

        