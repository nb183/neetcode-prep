class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def backtrack(current_sum, start, current_arr):
            if current_sum == target:
                ans.append(current_arr.copy())
                return

            if current_sum > target:
                return
            
            for index in range(start, len(nums)):
                elem = nums[index]
                current_arr.append(elem)
                backtrack(current_sum + elem, index, current_arr)
                current_arr.pop()

        backtrack(0, 0, [])
        return ans