class Solution:
    def minLength(self, s: str) -> int:
        
        stack = []
        for c in s:
            if c == 'B' and stack:
                if stack[-1] == 'A':
                    stack.pop()
                else:
                    stack.append(c)
            elif c == 'D' and stack:
                if stack[-1] == 'C':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        
        return len(stack)
