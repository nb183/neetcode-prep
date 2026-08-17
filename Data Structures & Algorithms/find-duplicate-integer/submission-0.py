class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lazy = quick = 0

        while True:
            lazy = nums[lazy]
            quick = nums[nums[quick]]

            if lazy == quick:
                break

        lazy2 = 0
        while lazy != lazy2:
            lazy = nums[lazy]
            lazy2 = nums[lazy2]

        return lazy