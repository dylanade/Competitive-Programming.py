class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l+r)//2
            hours_needed = 0
            
            for j in piles:
                hours_needed += ((j-1)//mid) + 1
                
            if hours_needed > h:
                l = mid + 1
            else:
                r = mid
                
        return l
    
    
"""
((j-1)//mid)+1 :  in this line why we have subtracted 1 from j and then added 1 ?

Solution:  suppose there are 10 = bananas, and mid = 3 
            so by dividing 10/3 gives  3.33333...., and koko
            can not eat half banana or partial banana, so we have 
            subtracted 1 so that now bananas = 9 and now totaltime will be 
            9 / 3 = 3 hours, now for the partial banana we subtracted 1. so 
            now we add +1 so that partial banana can be eaten in the additional 
            hour.
"""