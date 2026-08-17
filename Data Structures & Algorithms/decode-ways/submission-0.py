class Solution:
    def numDecodings(self, s: str) -> int:
        mp = {len(s): 1}
        def dfs(pos):
            if pos in mp:
                return mp[pos]
            if s[pos] == "0":
                return 0
            ans = dfs(pos + 1)
   
            if pos + 1 < len(s):
                num = int(s[pos:pos+2])
                if num > 9 and num < 27:
                    ans += dfs(pos+2)
            mp[pos] = ans
            return ans
          
        return dfs(0)