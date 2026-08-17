class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a, b = newInterval
        ans = []

        for interval in intervals:
            if a > interval[1]:
                ans.append(interval)
            elif b < interval[0]:
                ans.append([a, b])
                a, b = interval[0], interval[1]
            else:
                a = min(interval[0], a)
                b = max(interval[1], b)

        ans.append([a, b])
        return ans
