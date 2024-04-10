class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        a = max(nums)
        nums.remove(a)
        b = max(nums)
        nums.remove(b)
        c = max(nums)
        nums.remove(c)
        
        while (len(nums) >= 0):
            if b+c > a:
                return a+b+c
            elif (len(nums) == 0):
                return 0
            else:
                a = b
                b = c
                c = max(nums)
                nums.remove(c)