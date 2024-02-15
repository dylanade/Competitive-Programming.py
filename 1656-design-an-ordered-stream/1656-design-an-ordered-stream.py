class OrderedStream:

    def __init__(self, n: int):
        self.size = n+1
        self.stream = [None] * (self.size)
        self.current = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        end = 0
        
        for i in range(self.current, self.size):
            if not self.stream[i]:
                break
            end = i + 1
        start = self.current
        
        if end:
            self.current = end
        
        return self.stream[start:end]
        
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

