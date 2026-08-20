class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        cache = {}
        def dfs(i, rem_amount):
            if rem_amount == 0:
                return 1
            if i == n or rem_amount < 0:
                return 0
            
            if (i, rem_amount) in cache:
                return cache[(i, rem_amount)]
            
            # skip i:
            skip = dfs(i + 1, rem_amount)

            #include i
            include = dfs(i, rem_amount - coins[i])
            
            cache[(i, rem_amount)] = skip + include 

            return cache[(i, rem_amount)]

        return dfs(0, amount)
  
        