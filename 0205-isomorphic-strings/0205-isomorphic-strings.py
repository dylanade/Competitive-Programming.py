class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False
        
        iso_dic = {}
        
        for i in range(len(s)):
            if s[i] not in iso_dic:
                if t[i] in iso_dic.values():
                    return False
                iso_dic[s[i]] = t[i]
            elif iso_dic[s[i]] != t[i]:
                return False
        
        return True
