class Solution:
    def myPow(self, x: float, n: int) -> float:

        def findPow(x, n):
            if n == 0:
                return 1

            val = findPow(x, n//2)
            val = val * val
            if n & 1:
                val = val * x

            return val

        ans = findPow(x, abs((n)))
        if n < 0:
            ans = 1 / ans
        return ans


     

        