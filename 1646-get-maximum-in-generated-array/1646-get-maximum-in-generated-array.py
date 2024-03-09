class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0, 1]
        if n > 1:
            for i in range(2, n+1):
                if i % 2 == 0:
                    nums.append(nums[i//2])
                else:
                    j = int((i//2))
                    k = int(abs(i-j))
                    nums.append(nums[j] + nums[k])
        elif n == 0:
            return 0
        
        return max(nums)
    
            
            
        
        