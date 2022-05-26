class Solution:
    def isValid(self, s: str) -> bool:
        """
        go through characters in string, if the character is an opening bracket, then add it to the stack. If the character is a closing bracket then compare it to the top element
        of the stack. If they are matching brackets then pop the top opening bracket from the stack, else false.
        If the length of stack is 1 then false
        """
        
        # initialize the stack as list in python
        stack = list()
        # matching brackets hashmap
        matching_brackets = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        if len(s) == 1:
            return False
        else:
            for c in s:
                # if c is an open bracket, add to stack
                if c in matching_brackets.values():
                    stack.append(c)
                
                # else c is closed bracket, the top element of the stack must be its matching bracket else invalid string. Stack must also not be empty
                else:
                    if stack and stack[-1] == matching_brackets[c]:
                        stack.pop()
                    else:
                        return False
        
        # if the stack is empty at the end, then valid pairs
        if not stack:
            return True
        return False