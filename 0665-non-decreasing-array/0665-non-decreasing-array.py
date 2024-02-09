class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(1, n):
            if (nums[i] < nums[i-1]):
                count += 1
                if i < n-1 and i >= 2 and nums[i-2] > nums[i] and nums[i-1] > nums[i+1]:
                    return False
                
        return count <= 1
    