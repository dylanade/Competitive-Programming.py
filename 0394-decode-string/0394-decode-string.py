class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i]==']':
                cur_s = ""
                while stack[-1].isalpha():
                    cur_s = stack.pop() + cur_s
                stack.append(cur_s * int(stack.pop()))
                i += 1
            elif s[i].isdigit():
                k = ''
                while i<len(s) and s[i].isdigit():
                    k += s[i]
                    i += 1
                stack.append(k)
            elif s[i].isalpha():
                cur_s = ""
                while i<len(s) and s[i].isalpha():
                    cur_s += s[i]
                    i += 1
                stack.append(cur_s)
            else:
                i += 1
        return "".join(stack)    
            
            
                
            