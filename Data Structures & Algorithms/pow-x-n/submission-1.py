class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            return 1 / self.myPow(x, abs(n))

        val = self.myPow(x, n//2)
        val = val * val

        if n & 1:
            val = val * x

        return val



     

        