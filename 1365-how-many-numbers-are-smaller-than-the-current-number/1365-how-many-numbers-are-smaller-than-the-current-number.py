class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        bucket = [0]*102
        
        for i in range(len(nums)):
            bucket[nums[i]+1] += 1

        for i in range(1, 102): 
            bucket[i] += bucket[i-1]
        
        for i in range(len(nums)):
            nums[i] = bucket[nums[i]]
        
        return nums
        