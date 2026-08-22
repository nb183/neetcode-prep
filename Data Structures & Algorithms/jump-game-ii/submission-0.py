class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        l = r = 0

        while r < n - 1 :
            temp = r + 1
            for i in range(l, r + 1):
                r = max(r, i + nums[i])
            l = temp
            jumps += 1
        return jumps



 
                
        