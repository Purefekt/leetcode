"""
Get the leaf nodes in an array for both.

O(m+n) time where m is size of first tree and n is size of second tree
O(m + n) space since it depends on the size of leaf nodes.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def helper(node, leaf_arr):
            if not node:
                return
            
            if not node.left and not node.right:
                leaf_arr.append(node.val)
            
            helper(node.left, leaf_arr)
            helper(node.right, leaf_arr)

        leaf1 = []
        leaf2 = []

        helper(root1, leaf1)
        helper(root2, leaf2)

        if leaf1 == leaf2:
            return True
        else:
            return False
