"""
if both p and q are larger than the current node, then go to the right subtree
if both p and q are smaller than the current node, then go to the left subtree
if one is less and one is larger, this means the current node is the LCA
add code for when p or q equals the node itself, or when it is an ancestor of itself
O(n) time to traverse all nodes in worst case
O(1) space.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        pval = p.val
        qval = q.val
        
        node = root
        
        while node:
            if node.val == qval or node.val == pval:
                return node
            
            if node.val > qval and node.val > pval:
                node = node.left
            
            elif node.val < qval and node.val < pval:
                node = node.right
            
            else:
                return node
            