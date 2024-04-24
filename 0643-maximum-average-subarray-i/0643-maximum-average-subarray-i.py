class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # O(n*k) - Time Limit Exceeded
        # window_sum = sum(nums[:k])
        # for i in range(k, len(nums)+1):
        #     window_sum = max(sum(nums[i-k:i]), window_sum) 
        # return window_sum / k
        
        window_sum = sum(nums[:k])
        max_avg = window_sum / k
        
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            max_avg = max(max_avg, window_sum / k)
            
        return max_avg
        
        