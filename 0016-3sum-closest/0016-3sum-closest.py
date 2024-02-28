class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        
        min_dif = float('inf')
        min_sum = 0
        
        for i in range(len(nums)-1):
            j = i + 1
            k = n - 1
            
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                
                if sum == target:
                    return sum
                
                if sum < target:
                    j += 1
                else:
                    k -= 1
                
                dif = abs(sum-target)
                if dif < min_dif:
                    min_dif = dif
                    min_sum = sum
                    
        return min_sum
                    
                
        
        