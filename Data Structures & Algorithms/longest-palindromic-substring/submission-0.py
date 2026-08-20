class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxL = 0
        maxR = 0

        # odd palindromes:
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > maxR - maxL:
                    maxL, maxR = l, r
                l -= 1
                r += 1

        # even palindromes
        for i in range(n - 1):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > maxR - maxL:
                    maxL, maxR = l, r 
                l -= 1
                r += 1
                
        return s[maxL:maxR + 1]
            
        