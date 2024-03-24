class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1
        else:
            left, right, curr_sum = 0, 0, 0
            length = math.inf
    
            while (left <= right and right < len(nums)):
                if (curr_sum >= target):
                    length = min(length, right-left)
                    curr_sum -= nums[left]
                    left += 1
                else:
                    curr_sum += nums[right]
                    right += 1
       
            while (left <= right):
                if(curr_sum >= target):
                    length = min(length, right-left)
                    curr_sum -= nums[left]
                left += 1
       
            return 0 if (length == math.inf) else length