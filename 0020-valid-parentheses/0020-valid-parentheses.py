class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        mapping = {')':'(','}':'{',']':'['}
        
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack or (char in mapping and mapping.get(char) != stack[-1]):
                    return False
                stack.pop()
                
        return not stack
        