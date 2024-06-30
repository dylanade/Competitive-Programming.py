class UndergroundSystem:

    def __init__(self):
        self.travels = {}
        self.travel_times = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travels[id] = [stationName, t]
        
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if (self.travels[id][0], stationName) not in self.travel_times:
            self.travel_times[(self.travels[id][0], stationName)] = [0, 0]
        
        self.travel_times[(self.travels[id][0], stationName)][0] += t - self.travels[id][1]
        self.travel_times[(self.travels[id][0], stationName)][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time_travelled, count_travels = self.travel_times[startStation, endStation]
        return total_time_travelled/count_travels
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)