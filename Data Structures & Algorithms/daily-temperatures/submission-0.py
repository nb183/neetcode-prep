class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Bruteforce -> For each day, traverse through every other next day, before we find a warmer termperature day, and return the difference of the days. If no warmer days is found or if it is the last, day set the value to 0.
        # TC -> O(n^2) SC -> O(1)

        # Optimal -> We can traverse from right to left and mantain a striictly decreasing monotonic stack
        # TC -> O(n), SC -> O(n)


        n = len(temperatures)
        ans = [0] * n

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i) 
        return ans
            
        
            

        