"""
Dfs with recursion.
For each node, if we are at depth - 1, save the left and right nodes as tmp vars.
Create a new node for left and set the val as val, left node as left tmp and right node as None.
Create a new node for right and set the val as val, left node as None and right node as right tmp.
Return to break the loop.
Do this for all left and right children.
Write extra edge case for when depth == 1.

O(n) time since we can traverse all nodes at once.
O(d) space since the max height of recursive stack will be the depth-1.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def helper(node, d):
            if not node:
                return
            
            if d == depth-1:
                tmp_left = node.left
                tmp_right = node.right
                node.left = TreeNode(val, tmp_left, None)
                node.right = TreeNode(val, None, tmp_right)
                return
            
            helper(node.left, d+1)
            helper(node.right, d+1)
        
        if depth == 1:
            new_root = TreeNode(val, root, None)
            return new_root

        helper(root, 1)
        return root
