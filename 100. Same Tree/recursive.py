"""
Each node should be the same and all their subtrees as well.
Use a helper function to determine this recursively.
The helper function takes in the current node from the first and second tree.
If both are None, which means we have successfully reached leafs of both and return True.
If one tree still exists but the other does not, this means they are not equal and return false.
From each node, return helper on left and right and get the AND of both.

O(n) time to go over all nodes
O(n) space for stack
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def helper(first, second):
            if not first and not second:
                return True
            
            if not first and second:
                return False
            
            if first and not second:
                return False
            
            if first.val == second.val:
                return (helper(first.left, second.left) and helper(first.right, second.right))
        
        return helper(p,q)
        