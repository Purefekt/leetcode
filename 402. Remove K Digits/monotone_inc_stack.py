"""
Monotone increasing stack.
Build a stack which is in an increasing order.
Put a character into the stack, when we put the next, if this is larger than the previous element, then simply append.
Else, first remove all elements from the stack which are larger then it and then append the current element.
Do this k times and then simply keep appending.
NOTE: If we havnt removed k items, keep removing elements from the right side of the stack till k==0.
NOTE: Remove leading zeros from the stack. Do not use int conversion since it will exceed limit.

O(n) time. The outer loop runs for n time and the while loop runs for at max k times, this O(k+n) but k<=n thus 2n.
O(n) space for the stack
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for i in range(len(num)):
            while k>0 and stack and num[i] < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(num[i])

        while k>0 and stack:
            stack.pop()
            k -= 1
        
        while stack and stack[0] == "0":
            stack.pop(0)

        if not stack:
            return "0"
        return ''.join(stack)
