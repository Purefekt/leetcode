"""
Traverse the tree using backtracking dfs.
At any point the node itself can be the LCA and also p or q.
So set a var 'mid' to True if it is either p or q.
Next recursively run it on left and right subtree.
If atleast 2 of the 3, mid, left or right are True, we set result to that node.
Return left or right or mid for the function, since it is True if any one is true.

O(n) time since we traverse all nodes at most once.
O(n) space for the stack.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        res = None
        
        def helper(node):
            nonlocal res
            if not node:
                return False
            
            mid = False
            if node.val == p.val or node.val == q.val:
                mid = True
            
            left = helper(node.left)
            right = helper(node.right)

            if mid + left + right >= 2:
                res = node
            
            return left or right or mid

        helper(root)
        return res
