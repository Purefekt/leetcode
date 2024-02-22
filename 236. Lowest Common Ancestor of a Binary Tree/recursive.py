"""
Use a rexursive helper function which compares p.val and q.val against the current node.val.
If BOTH p.val and q.val are smaller than node.val, then continue the search on the left side.
If BOTH p.val and q.val are larger than node.val, then continue the search on the right side.
Else, the current node is the LCA since p and q are going in the opposite direction starting from this node.

O(n) time. We can at max visit all nodes
O(n) space for stack
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(node):
            if p.val < node.val and q.val < node.val:
                return helper(node.left)
            
            elif p.val > node.val and q.val > node.val:
                return helper(node.right)
            
            else:
                return node
        
        return helper(root)
        