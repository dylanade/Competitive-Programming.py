class Solution:
    def minSteps(self, n: int) -> int:
        import math

        def factors(a):
            maxFactor = 1
            for i in range(1, int(math.sqrt(a) + 1)):
                if a % i == 0:
                    if a // i != a:
                        maxFactor = max(maxFactor, a // i)
            return maxFactor
            
            
        def copy(n):
            ans = 0
            
            if n == 1:
                return 0
            
            while True:
                g = factors(n)
                if g == 1:
                    ans += n
                    break
                ans += n // g
                n = g
            
            return ans

        return copy(n)
