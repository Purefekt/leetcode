"""
Recursive.
For each node, we keep track of the current path which is the value at that node.
If node is null, simply return.
To update path, multiply it with 10 and add the node.val.
Check if this node is a leaf, if so then update the result.
Call on both left and right.

O(n) time since we check each node at most once.
O(h) space for the recursion stack which is the height of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        def helper(node, path):
            
            nonlocal res

            if not node:
                return

            path = path * 10 + node.val
            if not node.left and not node.right:
                res += path
            
            helper(node.left, path)
            helper(node.right, path)
        
        helper(root, 0)
        return res
