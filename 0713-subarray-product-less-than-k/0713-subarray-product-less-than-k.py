class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        windowSize = 0
        product = 1
        answer = 0
        right = 0
        
        while right < len(nums):
            product *= nums[right]
            
            while product >= k:
                product /= nums[windowSize]
                windowSize += 1
                
            answer += (right - windowSize + 1)
            right += 1
        
        return answer