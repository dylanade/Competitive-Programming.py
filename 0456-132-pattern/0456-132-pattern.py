class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        k = float('-inf')

        # Iterate through the array in reverse order
        for num in reversed(nums):
            # If we find a number smaller than k, 
            # it means we've found a valid pattern
            if num < k:
                return True
            # Keep updating k and popping elements from the stack
            while stack and stack[-1] < num:
                k = stack.pop()
            # Push the current number onto the stack
            stack.append(num)

        # If no valid pattern is found, return False
        return False