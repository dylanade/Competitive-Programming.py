class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        sum_all = sum(range(len(nums)+1))
        return sum_all - sum_nums
        