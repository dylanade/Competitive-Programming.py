class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def dfs(s):
            hashset = set(s)
            if len(hashset) < 2:
                return ""
            
            for i in range(len(s)):
                if not s[i].swapcase() in hashset:
                    sub_s1 = dfs(s[:i])
                    sub_s2 = dfs(s[i+1:])
                    return sub_s2 if len(sub_s2) > len(sub_s1) else sub_s1
            return s
        return dfs(s)
            
            
