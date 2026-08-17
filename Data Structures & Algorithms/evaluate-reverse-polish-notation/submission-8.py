class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        def evaluate(num1, num2, op):
            if op == "+":
                return num1 + num2
            elif op == "-":
                return num1 - num2
            elif op == "*":
                return num1 * num2
            else:
                return int(num1 / num2)

        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                result = evaluate(num1, num2, token)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]

            
            
        