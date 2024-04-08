"""
Monotonic decreasing stack.
When we push an element to the stack, we are going in the left direction.
This means we will always push smaller elements to the stack, thus we maintain a monotonic decreasing stack.
Now if we encounter a num which is > stack[-1], this means it must go to the right subtree.
But we need to place it at the current node, so we pop all elements < n, from the stack.
We place this element next.
But we also need to make sure we dont place an element to the right where a subtree's ancestor might be larger than the number.
Thus anytime we pop, we update a limit var, we can ONLY place an element to the right if that number is larger than the limit, to maintain BST property.

O(n) time to iterate over all nums once. Also we put all elements and pop them at once from the stack.
O(n) space for the stack.
"""

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        stack = []
        limit = 0

        for n in preorder:
            while stack and stack[-1] < n:
                limit = stack.pop()
            
            if n < limit:
                return False
            
            stack.append(n)
        
        return True
