class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        countGoodPairs = 0
        length = len(nums)

        for i in range(0, length):
            for j in range(0, length):
                if (nums[i] == nums[j] and i < j):
                    countGoodPairs += 1
                    
        return countGoodPairs
        