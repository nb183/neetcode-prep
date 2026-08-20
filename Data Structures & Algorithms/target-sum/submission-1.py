class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        cache = {}

        def dfs(i, cursum):
            if i == n:
                    return cursum == target

            if (i, cursum) in cache:
                return cache[(i, cursum)]

            
            cache[(i, cursum)] = dfs(i + 1, cursum + nums[i]) + dfs(i + 1, cursum - nums[i])
            return cache[(i, cursum)]

        return dfs(0, 0)
        