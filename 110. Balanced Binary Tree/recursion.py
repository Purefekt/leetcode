"""
Recursion.
Recursive function takes in the node and returns a tuple -> (status of balance, height).
base case return [True, 0] is node is null.
balanced will be True as long as abs(left height - right height) <= 1, else False.
Height will be max(left height, right height) + 1.
Return the balance in the end by passing root.

O(n) time to visit all nodes onces.
O(1) space.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node):

            if not node:
                return [True, 0]
            
            left = helper(node.left)
            right = helper(node.right)
            balanced = left[0] and right[0]
            if abs(left[1]-right[1]) > 1:
                balanced = False
            height = max(left[1], right[1]) + 1

            return [balanced, height]
        
        return helper(root)[0]
