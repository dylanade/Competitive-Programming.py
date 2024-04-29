class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            x += -1 if op == "--X" or op == "X--" else 1
        return x