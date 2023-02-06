"""
Use a stack with counts for consecutive same chars using 2d list = [[char, count]]
Go through the chars in s and maintain a stack. 
If char c is same as the last char added to the stack, increment the counter by 1
If char c is not same as the last char added, then append [c, 1] to the stack
Check if the top element of the stack's counter == k, if yes the pop from the stack
In the end our stack will have all the remaining chars and their counts in order, build the result using these

O(n) time to go through the input s
O(n) space to maintain stack
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []

        for i in range(len(s)):

            if stack:
                if s[i] == stack[-1][0]:
                    stack[-1][1] += 1
                else:
                    stack.append([s[i], 1])
            else:
                stack.append([s[i], 1])
            
            if stack[-1][1] == k:
                stack.pop()

        # build the output using stack
        res = ''
        for i in range(len(stack)):
            res += stack[i][0] * stack[i][1]
        
        return res
