class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        n = len(s)

        def check(l, r):
            res = 0
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    res += 1
                else:
                    break
                l -= 1
                r += 1
            return res
        
        for i in range(n):
            ans += check(i, i)
            ans += check (i, i + 1)

        
            
        return ans
