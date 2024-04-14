class Solution:
    def breakPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return ""
        else:
            for i in range(n//2):
                if s[i]!='a':
                    return s[0:i]+'a'+s[i+1:]
            return s[0:n-1]+'b'
                
        