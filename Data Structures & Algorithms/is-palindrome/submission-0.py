class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        S = []
        for c in s:
            if c.isalnum():
                S.append(c)
        S = "".join(S)
        print(S)
        n = len(S)
        for i in range(n//2):
            if S[i] != S[n-i-1]:
                return False
        return True


        