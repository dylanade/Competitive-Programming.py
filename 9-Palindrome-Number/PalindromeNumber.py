class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        return str_x == str_x[::-1]

#LINK: https://leetcode.com/problems/palindrome-number/submissions/1163190628
