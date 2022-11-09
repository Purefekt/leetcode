"""Recursive"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def postorder(node):
            if not node: return
            
            postorder(node.left)
            postorder(node.right)
            s.append(node.val)
        
        s = []
        postorder(root)
        
        return s
        