"""
Extra coins of less coins means the same.
Having 4 coins means that a node can give 3 and having 0 coins means a node needs 1.
Use dfs and find how much each node can exchange.
Null returns 0.

O(n) time to go over all nodes once.
O(n) space used by stack.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        def helper(node):
            nonlocal res

            if not node:
                return 0
            
            # number of extras
            left = helper(node.left)
            right = helper(node.right)

            res += abs(left) + abs(right)

            return (node.val-1) + left + right
        
        helper(root)
        return res
