class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * n
        k = 0
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    if nums[j] < nums[i]:
                        count[i] += 1
                        
        return count
        
        