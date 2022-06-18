"""
if both p and q are larger than the current node, then go to the right subtree
if both p and q are smaller than the current node, then go to the left subtree
if one is less and one is larger, this means the current node is the LCA
add code for when p or q equals the node itself, or when it is an ancestor of itself
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        stack = []
        
        stack.append(root)
        
        while stack:
            node = stack.pop()
            
            if p.val > node.val and q.val > node.val:
                stack.append(node.right)
            if p.val < node.val and q.val < node.val:
                stack.append(node.left)
            if (p.val >= node.val and q.val <= node.val) or (p.val <= node.val and q.val >= node.val):
                return node
        