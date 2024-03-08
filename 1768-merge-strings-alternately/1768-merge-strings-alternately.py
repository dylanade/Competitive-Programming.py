class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged, tail = [], []
        char1, char2 = list(word1), list(word2)
        p, q = len(word1), len(word2)

        if p > q:
            tail = char1[q:]
        else:
            tail = char2[p:]
        
        for i in range(min(p,q)*2):
            if i % 2 == 0:
                merged.append(char1[i//2])
            else:
                merged.append(char2[(i-1)//2])
        
        return "".join(merged + tail)
        
        
        
        