class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        while len(str2) > 0:
            if len(str1) < len(str2):
                str1, str2 = str2, str1

            if str1[:len(str2)] == str2:
                str1 = str1[len(str2):]
            else:
                return ""
            
        return str1