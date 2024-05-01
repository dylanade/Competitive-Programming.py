class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_sum = 0
        
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l]+nums[r]>max_sum:
                max_sum = nums[l]+nums[r]
            l += 1
            r -= 1

        return max_sum
  