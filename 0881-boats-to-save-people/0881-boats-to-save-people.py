class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = sorted(people,reverse=True)
        boat = 0
        l, r = 0, len(people)-1
        
        while l < r:
            if count[l] + count[r] <= limit:
                boat += 1
                l += 1
                r -= 1
            else:
                boat += 1
                l += 1
                
        if l == r:
            boat += 1
            
        return boat
                 
       
                    
                    
                    
        