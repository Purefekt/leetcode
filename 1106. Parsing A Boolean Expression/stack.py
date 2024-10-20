"""
Stack.
Build the stack by pushing only &, |, !, True, False and (.
Do not add commas.
When we hit a ), now we pull out all the values till the first open brackets.
Put them in an array, this is an array of booleans.
Then pop again to remove (.
Then pop again to get the operation.
If it is &, get the and of all and place this single boolean back into the stack.
If it is |, get the or of all and place this single boolean back into the stack.
If it is !, not all boolean and put all these boolean back into the stack.
The result will be the 0th (only element) in the remaining stack.

O(n) time to at max push and pop once for each element.
O(n) space used by stack.
""" 

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        stack = []
        for c in expression:
            if c == ',':
                continue
            elif c == ')':
                # pop till we get all
                cur_arr = []
                while stack[-1] != '(':
                    cur_arr.append(stack.pop())
                # remove (
                stack.pop()
                # get the operation
                op = stack.pop()
                if op == '&':
                    res = True
                    for val in cur_arr:
                        res = res and val
                    stack.append(res)
                elif op == '|':
                    res = False
                    for val in cur_arr:
                        res = res or val
                    stack.append(res)
                else:
                    for val in cur_arr:
                        if val == True:
                            stack.append(False)
                        else:
                            stack.append(True)
            else:
                if c == 'f':
                    stack.append(False)
                elif c == 't':
                    stack.append(True)
                else:
                    stack.append(c)
        
        return stack[0]
        