"""
Recursion.
If null node then return.
Set current node's left to helper(node.left) and same for right node.
If now this node becomes leaf node, check its val, if it is target, this node must also be null.
In this case return None else return the node.

O(n) time to go over each node at most once.
O(n) space used by recursion stack.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def helper(node):
            if not node:
                return node
            
            node.left = helper(node.left)
            node.right = helper(node.right)

            if not node.left and not node.right and node.val == target:
                return None
            
            return node

        return helper(root)
