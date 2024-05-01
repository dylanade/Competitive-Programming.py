class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = float('-inf')
        n = len(nums)
        
        r = n-1
        l = 0
        while l < (n//2):
            max_sum = max(max_sum, (nums[l]+nums[r]))
            l += 1
            r -= 1

        return max_sum