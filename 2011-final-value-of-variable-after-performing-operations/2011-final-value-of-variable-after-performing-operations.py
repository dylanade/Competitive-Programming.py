class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        
        for op in operations:
            if op == "--X":
                x -= 1
            elif op == "X++":
                x += 1
            elif op == "++X":
                x += 1
            elif op == "X--":
                x -= 1
            else:
                continue
        
        return x