class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            
            maxSum = max(curSum, maxSum)
            #curSum = max(curSum, 0)
            #maxSum = max(maxSum, curSum)
        
        return maxSum
        