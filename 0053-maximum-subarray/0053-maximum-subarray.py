class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current = 0
        for num in nums:
            if current < 0:
                current = 0
            current += num
            max_sum = max(current, max_sum)
        return max_sum
        