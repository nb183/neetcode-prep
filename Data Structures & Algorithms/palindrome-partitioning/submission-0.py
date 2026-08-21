class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        current = []

        def is_palin(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
                
        def dfs(i):
            if i == n:
                ans.append(current[:])
                return

            for j in range(i, n):
                if is_palin(i, j):
                    current.append(s[i: j + 1])
                    dfs(j + 1)
                    current.pop()
        dfs(0)
        
        return ans

        

            

        