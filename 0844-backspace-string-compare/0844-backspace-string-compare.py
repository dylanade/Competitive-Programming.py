class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def compare(a):
            stack = []
            for char in a:
                if char != '#':
                    stack.append(char)
                else:
                    if len(stack) > 0:
                        stack.pop()
            return stack
        
        return compare(s) == compare(t)