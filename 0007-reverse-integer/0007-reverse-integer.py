class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(abs(x))
        str_x = str_x[::-1]
        rev_x = int(str_x)
        
        if (rev_x < -2**(31) or rev_x > 2 ** (31) - 1):
            return 0
        else:
            if (x < 0):
                return -rev_x
            else:
                return rev_x
        