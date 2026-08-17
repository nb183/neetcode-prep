class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        nums.sort()
        def backtrack(i):
            if i == len(nums):
                if subset not in ans:
                    ans.append(subset[:])
                return
            subset.append(nums[i])    
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)
        
        backtrack(0)

        return ans
