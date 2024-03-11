class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = int(sqrt(c))
        left, right = 0, a
        
        while left <= right:
            ans = left**2 + right**2
            if ans < c:
                left += 1
            elif ans > c:
                right -= 1
            else:
                return True
            
        return False