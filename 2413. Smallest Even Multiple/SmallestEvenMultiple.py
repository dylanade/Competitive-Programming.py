class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """

        if (n % 2 == 0): 
            return n 
        return 2 * n

#LINK: https://leetcode.com/problems/smallest-even-multiple/submissions/1163715328
