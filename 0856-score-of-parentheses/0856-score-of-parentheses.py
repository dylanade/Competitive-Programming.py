class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        i = 0
        while i < len(s):
            if i+1<len(s) and s[i]=='(' and s[i+1]==')':
                score += 1
                i += 2
            elif s[i]=='(':
                stack.append(score)
                score = 0
                i += 1
            elif s[i]==')':
                if stack:
                    score = stack.pop() + 2*score
                i += 1

        return score
            
        
        
            