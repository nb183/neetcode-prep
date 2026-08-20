class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        cache = {}
        def dfs(i, curr_amount):
            if i == n:
                return 1 if curr_amount == amount else 0
            
            if curr_amount > amount:
                return 0
            
            if (i, curr_amount) in cache:
                return cache[(i, curr_amount)]
            
            # skip i:
            skip = dfs(i + 1, curr_amount)

            #include i
            include = dfs(i, curr_amount + coins[i])
            
            cache[(i, curr_amount)] = skip + include 

            return cache[(i, curr_amount)]

        return dfs(0, 0)
  
        