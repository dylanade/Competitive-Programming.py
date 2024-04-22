class RecentCounter:

    def __init__(self):
        self.request = collections.deque()
        

    def ping(self, t: int) -> int:
        self.request.append(t)
        start = t-3000
        
        while self.request[0] < start:
            self.request.popleft()
        
        return len(self.request)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)