# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        stack = [(root, False)]
        while stack:
            node, status = stack.pop()
            if not node.left and not node.right and status is True:
                res += node.val
            
            if node.left:
                stack.append((node.left, True))
            
            if node.right:
                stack.append((node.right, False))
        
        return res
