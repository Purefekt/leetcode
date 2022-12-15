"""
Create level order 2d array. 
For each level point the next to the next, except last one which points to None

O(n) time since we traverse all n nodes in the tree
O(n) space since we save all nodes in the level order array
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
        
        # get level order traversal and point to next
        level_order = []
        queue = [root]
        while queue:
            cur_lvl = []
            for i in range(len(queue)):
                node = queue.pop(0)
                cur_lvl.append(node)
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)
            level_order.append(cur_lvl)
        
        for level in level_order:
            if len(level) == 1:
                level[0].next = None
            else:
                for i in range(len(level)-1):
                    level[i].next = level[i+1]
        
        return root
                