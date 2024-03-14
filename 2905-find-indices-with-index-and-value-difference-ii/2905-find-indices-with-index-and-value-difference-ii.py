class Solution:
    def findIndices(self, nums: List[int], iD: int, vD: int) -> List[int]:
        if iD >= len(nums):
            return [-1, -1]
        
        minV, maxV = float('inf'), float('-inf')
        minI, maxI = 0, 0
        i = len(nums) - iD - 1
        j = len(nums) - 1
        
        while i >= 0:
            if nums[j] < minV:
                minV = nums[j]
                minI = j
                
            if nums[j] > maxV:
                maxV = nums[j]
                maxI = j
            
            if abs(nums[i] - minV) >= vD:
                return [i, minI]
            
            if abs(nums[i] - maxV) >= vD:
                return [i, maxI]
            
            i -= 1
            j -= 1
        
        return [-1, -1]
                    
    