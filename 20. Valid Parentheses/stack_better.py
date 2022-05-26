class Solution:
    def isValid(self, s: str) -> bool:
        """
        If character in string is a closing bracket, then check if stack is not empty and the top element (last element of the list in python) must be its matching bracket. Else False
        If the character is an opening bracket, add this to the top of stack (last element of the list in python)
        """
        
        stack = list()
        matching_brackets = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for c in s:
            # if c is a closing bracket
            if c in matching_brackets.keys():
                # if stack is not empty and the top element is its matching bracket
                if stack and stack[-1] == matching_brackets[c]:
                    # remove the corresponding matching bracket from the stack
                    stack.pop()
                # else invalid since either stack is empty which means the first element is a closing bracket (not valid) or the top element isnt its matching bracket
                else:
                    return False
            
            # else if c is an opening bracket, add it to the stack
            else:
                stack.append(c)
            
        # at the end of the for loop, if the stack is empty
        if not stack:
            return True
        return False
    