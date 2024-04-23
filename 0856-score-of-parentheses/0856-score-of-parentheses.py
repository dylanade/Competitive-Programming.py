class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        
        for c in s:
            if c=='(':
                stack.append(score)
                score = 0
            elif c==')':
                score = 1 if score==0 else score*2
                score = score + stack.pop()
            
        return score
    
#         stack = []
#         score = 0
#         i = 0
    
#         while i < len(s):
#             if i+1<len(s) and s[i]=='(' and s[i+1]==')':
#                 score += 1
#                 i += 2
#             elif s[i]=='(':
#                 stack.append(score)
#                 score = 0
#                 i += 1
#             elif s[i]==')':
#                 if stack:
#                     score = stack.pop() + 2*score
#                 i += 1

#         return score

            
        
        
            