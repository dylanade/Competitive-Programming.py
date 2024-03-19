from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        k = len(p)
        ans = []
        
        for i in range(k, len(s)+1):
            window = Counter(s[i-k:i])
            if window == target:
                ans.append(i-k)
                
        return ans
                
        
        