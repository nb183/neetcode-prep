class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}

        def solve(i, target):
            if (i, target) in dp:
                return dp[(i, target)]
            if target == 0:
                return True
            if i == len(nums):
                return False

            dp[(i, target)] = solve(i + 1, target - nums[i]) or solve(i + 1, target)

            return dp[(i, target)]
        
        S = sum(nums)
        if S & 1 == 1:
            return False
        return solve(0, S // 2 )