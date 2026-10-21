class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2)) != len(s3):
            return False

        dp = {}
        def solve(i, j):            
            if i == len(s1) and j == len(s2):
                return True

            if (i, j) in dp:
                return dp[(i, j)]

            first, second = False, False
            if i < len(s1) and s1[i] == s3[i + j]:
                first = solve(i + 1, j)

            if j < len(s2) and s2[j] == s3[i + j]:
                second = solve(i, j + 1)

            dp[(i, j)] = first or second
            return dp[(i, j)]

        return solve(0, 0) 

