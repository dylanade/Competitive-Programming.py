class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        i = 1
        
        while i < len(s):
            max_score = max(max_score, s[:i].count('0') + s[i:].count('1'))
            i += 1
        
        return max_score
        
        
        