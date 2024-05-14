class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        ans = 0
        
        for house in houses:
            i = bisect.bisect_left(heaters, house)
            q = abs(heaters[i-1]-house)
            if i<len(heaters): 
                q = min(q, abs(heaters[i]-house))
            if i+1<len(heaters): 
                q = min(q, abs(heaters[i+1]-house))
            ans = max(ans, q)
        return ans