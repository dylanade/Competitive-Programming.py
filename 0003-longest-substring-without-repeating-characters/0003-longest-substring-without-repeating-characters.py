from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        check = set()
        
        if len(s) == 0:
            return max_len
        
        while r < len(s):    
            if s[r] not in check:
                check.add(s[r])
                r += 1
                max_len = max(max_len, r-l)
            else:
                while l<r and s[r] in check:
                    check.remove(s[l])
                    l += 1
                check.add(s[r])
                r += 1
        return max_len