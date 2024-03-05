class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        varea = 0
        
        for i in range(len(points)-1):
            varea = max(varea, points[i+1][0]-points[i][0])
        return varea
            
        