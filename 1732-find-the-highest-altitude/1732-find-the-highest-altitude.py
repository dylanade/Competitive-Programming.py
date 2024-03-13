class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = h = 0
        for g in gain:
            h += g
            ans = max(ans, h)
        return ans 
        