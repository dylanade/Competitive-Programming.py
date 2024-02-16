class FrequencyTracker:

    def __init__(self):
        self.mapping = defaultdict(int)
        self.frequencies = defaultdict(int)
        

    def add(self, number: int) -> None:
        if self.frequencies[self.mapping[number]] > 0:
            self.frequencies[self.mapping[number]] -= 1
        self.mapping[number] += 1
        self.frequencies[self.mapping[number]] += 1
        

    def deleteOne(self, number: int) -> None:
        if self.mapping[number] > 0:
            self.frequencies[self.mapping[number]] -= 1
            self.mapping[number] -= 1
            self.frequencies[self.mapping[number]] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequencies[frequency] > 0
        
# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

