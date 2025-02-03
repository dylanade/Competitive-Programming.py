class Solution:
    def isPalindrome(self, x: int) -> bool:
        # reverse the number x, rev_x
        # compare reverse number with the x -> x == rev_x

        # mathematical way -> separate each digit in the number and rebuild the reversed number -> compare it

        # string way -> 
        return str(x)[::-1] == str(x)
        