"""
Stack.
Iterate through the string and place everything in the stack except when it is ')'.
When we hit ')', get all chars from stack till '(' and put them back in the stack, this will reverse it.

O(n) time to build the stack.
O(n) space, each letter enters and leaves stack once.
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []

        for c in s:
            if c == ')':
                cur = []
                while stack[-1] != '(':
                    cur.append(stack.pop())
                stack.pop()
                # put it back in the stack, this will cause it to reverse
                for char in cur:
                    stack.append(char)
            else:
                stack.append(c)
        
        return ''.join(stack)
