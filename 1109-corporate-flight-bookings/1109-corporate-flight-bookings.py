class Solution:
    def corpFlightBookings(self, b: List[List[int]], n: int) -> List[int]:
        prefix = [0]*(n+1)
        
        for first, last, seats in b:
            prefix[first-1] += seats
            prefix[last] -= seats
            
        cumulate = 0
        for i in range(1, n):
            prefix[i] += prefix[i-1]
            
        return prefix[:n]