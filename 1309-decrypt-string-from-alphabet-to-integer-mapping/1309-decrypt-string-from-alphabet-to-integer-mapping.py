class Solution:
    def freqAlphabets(self, s: str) -> str:
        answer = [] #stores answer as a char list
        n = len(s)  #stores length of s
        i = 0       #index to keep track of each char in s
        
        #iterate through the string, stop when we reach end of string
        while (i<n):
            
            #we are checking in advance if the char is '#' while keeping check of range
            if (i+2 < n and s[i+2] == "#"):
                current = int(s[i : i+2]) 
                answer.append(chr(current + 96))
                i+=3
                
            #keeping track of chars that do not have '#'
            else:
                answer += chr(int(s[i]) + 96)
                i+=1
                
        return ''.join(answer)