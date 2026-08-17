class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        last = intervals[0][1]
        for i in intervals[1:]:
            if i[0] < last:
                ans += 1
            else:
                last = i[1]

        return ans
