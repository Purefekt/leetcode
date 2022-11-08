"""
BFS. Add a node and swap its left and right.
O(n) time since we traverse all nodes
O(n) space since in the worst case we have all the nodes in the queue. 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return
        
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            #swap
            node.left, node.right = node.right, node.left
            
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        
        return root
        