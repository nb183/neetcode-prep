class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp [0] = True

        matches = [0]
        for i in range(1, n + 1):
            for j in matches:
                if s[j:i] in wordDict:
                    dp[i] = True
                    matches.append(i)
                    break
        
        return dp[n]