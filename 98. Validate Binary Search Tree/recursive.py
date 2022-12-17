"""
Recursive.
Create a recursive func validate which takes in a node, its lower bound and upper bound
If the node is a leaf node, return True since it is a BST
If the node value is lower or eq to low or high or eq to high, then return False
return the AND boolean value of all its children
Start with root, -inf for low, +inf for high

O(n) time to visit all nodes once
O(n) space to store all nodes of tree in the stack in the worst case
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low, high):

            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            
            # run for both sides
            return (validate(node.left, low, node.val) and validate(node.right, node.val, high))
        
        return validate(root, -inf, inf)
        