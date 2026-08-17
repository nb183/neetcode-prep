class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(l, r, current_str):
            if l == n and r == n:
                ans.append(current_str)
                return

            if l < n:
                backtrack(l + 1, r, current_str + "(")
            if r < l:
                backtrack(l, r + 1, current_str + ")")
        
        backtrack(1, 0, "(")
        return ans


        