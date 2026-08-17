class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        first = 0
        second = 0

        n = len(nums)

        for i in nums:
            first ^= i
        
        for j in range(n+1):
            second ^= j

        return first ^ second
        