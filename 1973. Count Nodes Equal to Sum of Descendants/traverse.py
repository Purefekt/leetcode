"""
Traverse the tree and for each node, return its left sum + right sum + its own value.
Also track the number of nodes where node.val == left + right.

O(n) time to visit all nodes once.
O(n) space for recursive stack.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def helper(node):
            nonlocal res

            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            if left + right == node.val:
                res += 1
            return left + right + node.val
        
        helper(root)
        return res
