class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Bruteforce -> a funky solution :)
        if digits == "":
            return []
        mp = {}
        mp["2"] = ["a", "b", "c"]
        mp["3"] = ["d", "e", "f"]
        mp["4"] = ["g", "h", "i"]
        mp["5"] = ["j", "k", "l"]
        mp["6"] = ["m", "n", "o"]
        mp["7"] = ["p", "q", "r", "s"]
        mp["8"] = ["t", "u", "v"]
        mp["9"] = ["w", "x", "y", "z"]

        ans = []
        curr = []
        n = len(digits)
        def dfs(i):
            if i == n:
                ans.append("".join(curr))
                return
            print(i)
            
            for c in mp[digits[i]]:
                curr.append(c)
                dfs(i + 1)
                curr.pop()
        
        dfs(0)

        return ans




        