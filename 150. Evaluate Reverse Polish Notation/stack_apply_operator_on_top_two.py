"""
Create a stack. If we have a number, add it to the stack. If it is an operator, pop the 2 elements from the stack, apply the operator and push the result onto the stack. Repeat for all elements in tokens.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # map operator strings to operator function
        operators_map = {
            '+': operator.add,
            '-': operator.sub,
            '/': operator.truediv,
            '*': operator.mul
        }
        
        stack = []
        
        for n in tokens:
            if n not in operators_map.keys():
                stack.append(n)
            else:
                operand_1 = int(stack.pop())
                operand_2 = int(stack.pop())
                
                operation = math.trunc(operators_map[n](operand_2, operand_1))
                
                stack.append(operation)
        
        # at the end stack will have a single value which will be the output
        return stack[0]
    