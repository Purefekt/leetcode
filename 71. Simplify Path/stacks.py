"""
Use stack to build the path.
Before building the path filter the tokens by splitting through '/', getting rid of empty string tokens
if we get a '..', pop from stack, 
if we get a '.', do nothing.
else append to the stack

O(n) time to go over the string 
O(n) space to store the intermediate arrays
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path_tokens = path.split('/')
        # get rid of all tokens of len<1
        path_tokens_filter = []
        for token in path_tokens:
            if len(token) > 0:
                path_tokens_filter.append(token)
        
        # use stack
        stack = []
        for token in path_tokens_filter:
            if token == '..':
                if stack:
                    stack.pop()
            elif token == '.':
                continue
            else:
                stack.append(token)
        
        res = '/' + '/'.join(stack)
        return res
