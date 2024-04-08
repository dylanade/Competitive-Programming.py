class Solution:
    def corpFlightBookings(self, b: List[List[int]], n: int) -> List[int]:
        prefix = [0]*(n+1)
        
        for first, last, seats in b:
            prefix[first-1] += seats
            prefix[last] -= seats
            
        for i in range(1, n):
            prefix[i] += prefix[i-1]
            
        return prefix[:n]
    
        res = [0] * n

#         for start, end, seats in bookings:
#             start_ = start - 1
#             end_ = end - 1
#             res[start_] += seats
#             if end < n:
#                 res[end] -= seats  
#         return accumulate(res)