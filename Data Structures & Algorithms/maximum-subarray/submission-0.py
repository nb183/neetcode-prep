class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]

        current = 0

        for num in nums:
            if current < 0:
                current = 0
            current += num

            maximum = max(maximum, current)

        return maximum