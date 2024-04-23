class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if not token in "+-*/":
                stack.append(int(token))
            else:
                if stack:
                    evaluate = 0
                    num1, num2 = stack.pop(), stack.pop()
                    if token == '+':
                        evaluate = num2 + num1
                    elif token == '-':
                        evaluate = num2 - num1
                    elif token == '*':
                        evaluate = num2 * num1
                    elif token == '/':
                        evaluate = int(num2/num1)
                    stack.append(evaluate)
                    
        return stack[0]