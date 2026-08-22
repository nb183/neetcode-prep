class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        i = 0

        for i in range(n):
            for j in range(1, nums[i] + 1):
                if dp[i] and i + j < n:
                    dp[i + j] = True
        
        return dp[n - 1]



