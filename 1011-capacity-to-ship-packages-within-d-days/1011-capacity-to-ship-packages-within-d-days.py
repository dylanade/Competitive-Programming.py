class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def get_sum(current):
            total, running_sum = 0, 0
            for i in weights:
                if running_sum + i <= current:
                    running_sum += i  
                else:
                    total += 1  
                    running_sum = i   
            return total+1 if running_sum else total 
        
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low+high)//2
            if get_sum(mid) > days:
                low = mid+1 
            else:
                high = mid-1 
        return low 