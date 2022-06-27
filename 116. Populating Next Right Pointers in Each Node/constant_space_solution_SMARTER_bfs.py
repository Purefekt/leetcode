"""
Constant space solution.
Use a pointer current and start at the root. Use a pointer next at the start of the next level. Which is current.left
set the left child.next to point to right child
set the right child to point to its PARENT'S next's left child (if it exists)
increment the current node to the next

if current node becomes null (this is after we set current node to next), this means the level is over.
Now we set current node to the start of the next level and set the start of the next level to the next level which is left of the start of the current level node.
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
            return None
        
        curr_node = root
        next_level_start_node = curr_node.left
        
        while curr_node and next_level_start_node:
            curr_node.left.next = curr_node.right
            
            if curr_node.next:
                curr_node.right.next = curr_node.next.left
            
            curr_node = curr_node.next
            
            if not curr_node:
                curr_node = next_level_start_node
                next_level_start_node = curr_node.left
        
        return root
    