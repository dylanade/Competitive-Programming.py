class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * (n+1)
        
        for start, end, direction in shifts:
            if direction==0:
                direction = -1
            prefix[start] += direction
            prefix[end+1] -= direction  
            
        accumulated = 0                        
        result = []
        for i in range(n):
            accumulated += prefix[i]    
            chr_num = ord(s[i]) - ord('a')         
            chr_num = (chr_num + accumulated) % 26  
            result.append(chr(chr_num + ord('a'))) 
        
        return ''.join(result)
        