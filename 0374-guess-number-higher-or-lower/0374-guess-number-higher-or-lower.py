# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lowerbound, upperbound = 0, n
        while lowerbound < upperbound:
            median = (upperbound+lowerbound) // 2
            result = guess(median)
            if result == 1:
                lowerbound = median +1
            elif result == -1:
                upperbound = median-1
            elif result == 0:
                return median
        return lowerbound
        