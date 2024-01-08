"""
Recursively traverse the BST.
If node is none, return 0.
If the node.val is in the ranger, add node.val to total and return the sum of left and right nodes.
Elif the node.val is less than low, this means there can only be valid numbers on the right subtree.
Elif the node.val is larger than low, this means there can only be valid numbers on the left subtree.

O(n) time to traverse all nodes at most once.
O(n) space for stack.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def helper(node):
            if not node:
                return 0
            
            total = 0
            if low <= node.val <= high:
                total += node.val + helper(node.left) + helper(node.right)
            
            elif node.val < low:
                total += helper(node.right)
            
            elif node.val > high:
                total += helper(node.left)
            
            return total
        
        return helper(root)
