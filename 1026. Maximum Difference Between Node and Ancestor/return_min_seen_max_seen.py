"""
Each node will send a tuple [max value seen so far, min value seen so far].
A leaf node returns [node.val, node.val].
At each node, get both the values from the left subtree and both the values from the right subtree.
update result to be max of current result, absolute diff between current node.val and min from left and right, absolute diff between current node.val and max from left and right.
add current node to left vals + right vals array, now it has 5 values.
return [min, max] of these 5 values.

O(n) time to go over all nodes onces.
O(n) space for the stack
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        def helper(node):
            nonlocal res

            # if this is a leaf node
            if not node.left and not node.right:
                return [node.val, node.val]
            
            left_vals = []
            if node.left:
                left_vals = helper(node.left)

            right_vals = []
            if node.right:
                right_vals = helper(node.right)
            
            combined = left_vals + right_vals
            
            res = max(
                res,
                abs(node.val - max(combined)),
                abs(node.val - min(combined))
            )

            combined.append(node.val)

            return [max(combined), min(combined)]
        
        helper(root)
        return res
        