class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = {}
        def dfs(idx, prev_idx):
            if idx == n:
                return 0
            
            if (idx, prev_idx) in dp:
                return dp[(idx, prev_idx)]

            res = 0

            res = dfs(idx + 1, prev_idx)

            if prev_idx == -1 or nums[idx] > nums[prev_idx]:
                res = max(1 + dfs(idx + 1, idx), res)

            dp[(idx, prev_idx)] = res
            return res



        return dfs(0, -1)


        