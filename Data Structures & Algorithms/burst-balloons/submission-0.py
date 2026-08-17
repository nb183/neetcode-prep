class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        def solve(l, r):
            if l > r:
                return 0

            if dp[l][r] != 0:
                return dp[l][r]

            best, l_val, r_val = 0, nums[l - 1], nums[r + 1]

            for i in range(l, r + 1):
                coins = l_val * nums[i] * r_val
                coins += (solve(l, i - 1) + solve(i + 1, r))
                best = max(best, coins)

            dp[l][r] = best
            return best

        return solve(1, n - 2)



