class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        cache = {}

        def dfs(i, cursum):
            if i == n:
                if cursum == target:
                    return 1
                return 0

            if (i, cursum) in cache:
                return cache[(i, cursum)]

            
            count = dfs(i + 1, cursum + nums[i])
            count += dfs(i + 1, cursum - nums[i])
            cache[(i, cursum)] = count

            return count

        ans = dfs(0, 0)
        return ans
        