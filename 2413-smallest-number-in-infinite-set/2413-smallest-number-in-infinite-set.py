class SmallestInfiniteSet:
    def __init__(self):
        self.cur = 1
        self.s = set()

    def popSmallest(self):
        if self.s:
            smallest = min(self.s)
            self.s.discard(smallest)
            return smallest
        else:
            self.cur += 1
            return self.cur - 1

    def addBack(self, num):
        if self.cur > num:
            self.s.add(num) 