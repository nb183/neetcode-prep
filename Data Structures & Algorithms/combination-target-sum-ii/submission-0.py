class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtrack(start, curr_sum, curr_arr):
            if curr_sum == target:
                ans.append(curr_arr.copy())
                return

            if curr_sum > target:
                return

            for idx in range(start, len(candidates)):
                elem  = candidates[idx]
                if idx > start and elem == candidates[idx - 1]:
                    continue
                curr_arr.append(elem)
                backtrack(idx + 1, curr_sum + elem, curr_arr)
                curr_arr.pop()

        backtrack(0, 0, [])
        return ans