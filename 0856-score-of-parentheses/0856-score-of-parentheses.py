class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        
        for c in s:
            if c=='(':
                stack.append(score)
                score = 0
            else:
                score = 1 if score==0 else score*2
                score = score + stack.pop()
            
        return score
