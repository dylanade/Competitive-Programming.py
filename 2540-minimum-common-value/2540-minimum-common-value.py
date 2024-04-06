class Solution:
    def getCommon(self, a: List[int], b: List[int]) -> int:
        i, j = 0, 0
        
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                return a[i]
            elif a[i] < b[j]:
                i += 1
            elif b[j] < a[i]:
                j += 1
            else:
                i += 1
                j += 1
                
        return -1
            