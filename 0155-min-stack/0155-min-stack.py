class MinStack:
    class Node:
        def __init__(self, val, minimum):
            self.val = val
            self.min = minimum
                
    def __init__(self):
        self.stack = []
    
    def push(self, val: int) -> None:
        if self.stack:
            minimum = min(self.stack[-1].min, val)
            self.stack.append(self.Node(val, minimum))
        else:
            self.stack.append(self.Node(val, val))

    def pop(self) -> None:
        return self.stack.pop().val

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()