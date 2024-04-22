class RecentCounter:

    def __init__(self):
        self.array = []
        
    def ping(self, t: int) -> int:
        self.array.append(t)
        count = 0
        for i in self.array:
            if i >= (t-3000) and i <= t:
                count += 1
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)