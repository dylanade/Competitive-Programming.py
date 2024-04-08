class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_left = [0] * n
        prefix_right = [0] * n
        
        sum_left = 0
        for i in range(n):
            sum_left += nums[i]
            prefix_left[i] = sum_left
            
        sum_right = 0
        for i in range(n-1, -1, -1):
            sum_right += nums[i]
            prefix_right[i] = sum_right
        
        for i in range(n):
            if prefix_right[i] == prefix_left[i]:
                return i

        return -1
        
        