class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for log in logs:
            if log not in ['./', '../']:
                stack.append(log)
            elif log in ['./', '../']:
                if log == './':
                    continue
                if log == '../' and stack:
                    stack.pop()
                else:
                    continue

        return len(stack)