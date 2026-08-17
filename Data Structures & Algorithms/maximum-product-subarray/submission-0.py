class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        cmin = cmax = 1

        for num in nums:
            if num == 0:
                cmin = cmax = 1
                continue
            temp_max = cmax
            cmax = max(cmax*num, cmin*num, num)
            cmin = min(cmin*num, temp_max*num, num)
            ans = max(cmax, ans)
        return ans