"""
BFS level order

O(n) time to go over all nodes
O(n) space to store
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return

        level_order = []
        queue = [root]
        while queue:
            cur_level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                for child in node.children:
                    queue.append(child)
                cur_level.append(node.val)
            level_order.append(cur_level)
        
        return level_order
                