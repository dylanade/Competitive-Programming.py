class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return x_str[::-1] == x_str
        