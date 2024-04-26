class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        k = float('-inf')

        for num in reversed(nums):
            if num < k:
                return True
            while stack and stack[-1] < num:
                k = stack.pop()
            stack.append(num)

        return False