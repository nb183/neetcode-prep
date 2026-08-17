class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1,  max(piles)
        ans = end
        while start <= end:
            mid = start + (end - start) // 2
            hrs = 0
            for x in piles:
                hrs += (x - 1) // mid + 1 

            if hrs <= h:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1

        return ans


        