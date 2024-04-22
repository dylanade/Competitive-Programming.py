class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(','}':'{',']':'['}
        
        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack or (char in mapping and mapping.get(char) != stack[-1]):
                    return False
                stack.pop()
                
        return not stack
        
        