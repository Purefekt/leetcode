"""
Using pointers to achieve constant time.
The root will point next to None
For all children of a node, next for left child will simply be the right child
next for right child will either be parent's next left (if parents next isnt None) else it will be None (right most node of a level)

O(n) time to go through all nodes
O(1) space
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return
        
        queue = [root]
        root.next = None
        while queue:
            node = queue.pop(0)
            
            # means both children exits
            if node.left:

                # left child next
                node.left.next = node.right

                # right child next
                if node.next:
                    node.right.next = node.next.left
                else:
                    node.right.next = None
                
                # add children to queue
                queue.append(node.left)
                queue.append(node.right)
        
        return root
