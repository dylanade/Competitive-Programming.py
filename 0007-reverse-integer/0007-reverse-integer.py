class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(abs(x))
        str_x = str_x[::-1]
        rev_x = int(str_x)
        
        if (x < 0):
            if (-rev_x < -2**(31)):
                return 0
            return -rev_x
        else:
            if (rev_x > 2**(31) - 1):
                return 0
            return rev_x
        