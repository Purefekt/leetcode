"""
use stack. Start at root and check a node. If the node == val, return. Else if that node is larger then the val, then the right subtree is discarded. If that node is smaller than val, then the left sub tree is discarded.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        stack = collections.deque()
        output = []
        
        stack.append(root)
        
        while stack:
            node = stack.pop()
            
            if node:
                if node.val == val:
                    return node
                if node.val > val:
                    stack.append(node.left)
                if node.val < val:
                    stack.append(node.right)
            
        return None
    