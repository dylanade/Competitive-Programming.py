class MyCircularDeque:
    def __init__(self, k: int):
        self.data = [None] * (k + 1)
        self.size = k + 1
        self.head = 0
        self.tail = 1

    def _next(self, index):
        return (index + 1) % self.size

    def _prev(self, index):
        return (index - 1) % self.size

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.head] = value
        self.head = self._prev(self.head)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.tail] = value
        self.tail = self._next(self.tail)
        return True        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.data[self.head] = None
        self.head = self._next(self.head)
        return True
  
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.data[self.tail] = None
        self.tail = self._prev(self.tail)
        return True        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self._next(self.head)]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self._prev(self.tail)]

    def isEmpty(self) -> bool:
        return self._next(self.head) == self.tail

    def isFull(self) -> bool:
        return self.head == self.tail

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()