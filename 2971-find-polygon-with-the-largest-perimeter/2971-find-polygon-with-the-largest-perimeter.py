class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = sum(nums)
        
        for num in nums:
            if num >= ans - num:
                ans -= num
            else:
                return ans
            
        return -1