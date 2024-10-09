"""
Stack.
Append ( to stack.
If we get a ), if the top element is (, then pop. Since they cancel out.
Else add to stack.
Return size of stack, this is all unmatched brackets.

O(n) time.
O(n) space.
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        for c in s:
            if c == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack)
