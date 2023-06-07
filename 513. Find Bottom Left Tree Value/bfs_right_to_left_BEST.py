"""
run BFS but from right to left.
The last node encountered will be the left most node in the last level

O(n) time to go over all nodes
O(1) space to store the res
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        res = None

        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                res = node.val
            
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        
        return res
