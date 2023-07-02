"""
Use dfs to get the depth at each node and save in a memo hashmap.
For a given node, the max depth is the max(left, right) + 1.

O(n) time to go through all nodes once.
O(n) space for stack.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        memo = {}
        
        def helper(node, depth):
            if not node:
                return depth
            
            memo[node] = max(helper(node.left, depth+1), helper(node.right, depth+1))
            return memo[node]
        
        return helper(root, 0)
        