class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(seen, current_list):
            if len(current_list) == len(nums):
                ans.append(current_list[:])
                return
            for num in nums:
                if num in seen:
                    continue
                current_list.append(num)
                seen.add(num)
                backtrack(seen, current_list)
                seen.remove(num)
                current_list.pop()

        backtrack(set(), [])
        return ans