class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count_seconds = 0
        
        for i in range(len(timeSeries) - 1):
            if timeSeries[i] + duration >= timeSeries[i+1]:
                count_seconds += timeSeries[i+1] - timeSeries[i]
            else:
                count_seconds += duration
                
        return count_seconds + duration
        