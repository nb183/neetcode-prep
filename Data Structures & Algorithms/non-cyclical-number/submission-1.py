class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sum_of_squares(num):
            ans = 0

            while num != 0:
                last = num % 10
                num = num // 10
                ans += last * last
            return ans
        
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum_of_squares(n)
            if n == 1:
                return True

        return False


        