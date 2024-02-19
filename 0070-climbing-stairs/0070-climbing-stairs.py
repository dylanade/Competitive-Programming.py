class Solution:
    def climbStairs(self, n: int) -> int:
        a, b, r = 1, 2, 0
        
        if (n == 1):
            return 1
        elif (n == 2):
            return 2
        else:
            for i in range(3, n + 1):
                r = a + b
                a = b
                b = r
                
        return r