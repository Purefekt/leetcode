"""
Stack.
First clean the data by creating numbers and removing whitespaces.
[10 - 10] -> [10, '-', 10]
Next use a stack to evaluate all brackets.
If closed bracket appears, pop and create equation from all elements in stack till we see an open bracket.
Then evaluate the final stack which will have no brackets.
Add leading '+' to simplify calculation.

O(n) time to add and pop from stack once for all elements.
O(n) space used by stack.
"""

class Solution:
    def calculate(self, s: str) -> int:

        # identify individual numbers and remove wwhitespaces
        this_num = ""
        new_s = []
        for c in s:
            if c == '-' or c == '+' or c == ' ' or c=='(' or c==')':
                if c == ' ':
                    continue
                if this_num:
                    new_s.append(int(this_num))
                new_s.append(c)
                this_num = ''
            else:
                this_num += c
        if this_num:
            new_s.append(int(this_num))
        
        stack = []
        for c in new_s:
            if c == ')':
                eq = []
                while stack[-1] != '(':
                    top = stack.pop()
                    eq.append(top)
                eq = eq[::-1]
                # add leading + if the first element is positive
                if eq[0] != '-':
                    eq.insert(0, '+')
                # get result by adding/sub all numbers
                result = 0
                for i in range(0, len(eq), 2):
                    if eq[i] == '+':
                        result += eq[i+1]
                    else:
                        result -= eq[i+1]
                # remove the open bracket
                stack.pop()
                # add result back to the stack
                stack.append(result)
            else:
                stack.append(c)
        
        # simply evaluate this stack 
        if stack[0] != '-':
            stack.insert(0, '+')
        
        result = 0
        for i in range(0, len(stack), 2):
            if stack[i] == '+':
                result += stack[i+1]
            else:
                result -= stack[i+1]
        
        return result
