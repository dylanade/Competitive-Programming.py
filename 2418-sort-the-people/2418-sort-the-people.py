class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        swapped = False
        n = len(heights)
        
        for i in range(n):
            for j in range(n-1):
                if heights[j] < heights[j+1]:
                    swapped = True
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
                    
            if not swapped:
                return names
        
        return names
    
    def bubbleSort(self, heights: List[int]) -> List[int]:  
        swapped = False
        n = len(heights)
        
        for i in range(n):
            for j in range(n-1):
                if heights[j] < heights[j+1]:
                    swapped = True
                    heights[j], heights[j+1] = heights[j+1], heights[j]
            
            if not swapped:
                return heights
        
        return heights
    
  