from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)
        starts = [start for start, _, _ in jobs]

        dp = [-1] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            start, end, p = jobs[i]

            j = bisect_left(starts, end)

            not_take = dp[i + 1]
            take = dp[j] + p

            dp[i] = max(take, not_take)

        return dp[0]
