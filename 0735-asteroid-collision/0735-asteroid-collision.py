class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if abs(a) > abs(stack[-1]): 
                    stack.pop()
                    continue
                elif abs(a) == abs(stack[-1]):
                    stack.pop()
                break
            else:
                stack.append(a)
        
        return stack
