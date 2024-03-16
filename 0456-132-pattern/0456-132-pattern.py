class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        last = float(-10**11)
        
        for num in reversed(nums):
            if num < last:
                return True
            while stack and stack[-1] < num:
                last = stack.pop()
            stack.append(num)
            
        return False