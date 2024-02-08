class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        targets = []
        
        for i in range(1, area+1):
            if (area % i == 0):
                if (i >= area//i):
                    coord = []
                    coord.append(i)
                    coord.append(area//i)
                    targets.append(coord)
          
        min_diff = abs(targets[0][0] - targets[0][1])
        ans = targets[0]
        
        for target in targets:
            diff = abs(target[0] - target[1])
            if (diff < min_diff):
                min_diff = diff
                ans = target
                
        return ans
                
            
        