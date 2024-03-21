class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        for x, y in [[a, b], [b, a]]:
            i, j = 0, len(x)-1
            
            while x[i]==y[j] and i<len(x) and j>0:
                i += 1
                j -= 1
                
            midx = x[i:j+1]
            midy = y[i:j+1]
            
            if (midx==midx[::-1] or midy==midy[::-1]):
                return True
            
        return False    
        
        #prefixes of a
        #u
        #ul
        #ula
        #ulac
        #...
        #ulacfd
        
        #suffixes of a
        #u
        #lu
        #alu
        #zalu
        #izalu
        