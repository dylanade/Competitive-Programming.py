class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answers = list()

        def addParenthesis(current, opened, closed):
            if len(current) == n*2:
                answers.append(current)
            if opened < n:
                addParenthesis(current + '(', opened+1, closed)
            if closed < n and closed < opened:
                addParenthesis(current + ')', opened, closed+1)
            return None

        addParenthesis('(', 1, 0)
        return answers  
                
        