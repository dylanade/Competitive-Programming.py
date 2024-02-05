import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_s = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                clean_s += char
                
        s = clean_s.lower()
        return s == s[::-1]
        