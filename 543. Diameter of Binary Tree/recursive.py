"""
Find the max diameter at each node, which is the path length of the node.left+1 + node.right+1.
The recursiv function returns 0 if the node is null.
get the left and right. update the result to the max of result and left + right
return max(left, right) + 1. This means we take the maximum path from either side and add 1 for the edge which it connects to.
The result variable is the diameter at each node whereas the return value is the maximum path sum from that node.

O(n) time to go over all nodes once.
O(n) space for stack
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def helper(node):
            nonlocal res

            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)

            res = max(res, left+right)

            return max(left, right) + 1
        
        helper(root)
        return res
        