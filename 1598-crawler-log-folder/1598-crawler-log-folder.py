class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        commands = ['./', '../']
        
        for log in logs:
            if log in commands:
                if log == './':
                    continue
                elif log == '../' and stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(log)

        return len(stack)