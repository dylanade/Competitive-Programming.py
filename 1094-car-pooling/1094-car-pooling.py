class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0] * 1001
        for passengers, start, end in trips:
            prefix[start] += passengers
            prefix[end] -= passengers
        
        total = 0
        for x in prefix:
            total += x
            if total > capacity:
                return False
        
        return True
            
            
            