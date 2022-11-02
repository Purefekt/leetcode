"""
Use operator class and use hashmap for cleaner string to operator mapping. add, sub, mul, trudiv
Iterator over all tokens, add them to stack if they are a number.
If a token is an operator, pop top 2 elements of the stack, apply the operation and push the result to the top of stack
At the end of the loop, the stack will contain a single element, the answer
O(n) time since we go through all tokens once in one pass
O(n) space, in the worst case all the numbers are in the stack. Due to how this notation works, there can never be more than n/2 numbers in a token list of n elements. Thus using n/2 space.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operator_map = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        
        stack = []
        
        for t in tokens:
            if t not in operator_map:
                stack.append(int(t))
            else:
                operatorr = operator_map[t]
                op2 = stack.pop()
                op1 = stack.pop()
                
                result = int(operatorr(op1, op2))
                stack.append(result)
        
        return stack[0]
    