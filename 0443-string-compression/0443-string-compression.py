class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        
        compression = []
        
        while j < len(chars):
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            
            compression.append(chars[i])
            if i+1 != j:
                for digit in str(j-i):
                    compression.append(digit)
                
            i = j
            
        chars[:] = compression
        return len(compression)
        