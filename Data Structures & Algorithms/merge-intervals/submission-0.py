class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        pi, pj = intervals[0]
        for i, j in intervals[1:]:
            if i > pj:
                ans.append([pi, pj])
                pi, pj = i, j
            elif i <= pj and j > pj:
                pj = j
        print(ans)
        if len(ans) ==0 or pi != ans[-1][0] and pj != ans[-1][1]:
            ans.append([pi, pj])
        return ans

