class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        s_set = set(s)

        for i in range(len(s)):
            if s[i].swapcase() not in s_set:
                subs1 = self.longestNiceSubstring(s[:i])
                subs2 = self.longestNiceSubstring(s[i+1:])
                if len(subs1) >= len(subs2):
                    return subs1
                return subs2
        return s
                
                