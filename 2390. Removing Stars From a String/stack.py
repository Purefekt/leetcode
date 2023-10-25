"""
Stack.
Add letter to stack if it isnt *.
When a *, then pop from stack.

O(n) time to iterate over the input once.
O(n) space for stack
"""

class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []

        for c in s:
            if c != '*':
                stack.append(c)
            else:
                stack.pop()
        
        return ''.join(stack)
