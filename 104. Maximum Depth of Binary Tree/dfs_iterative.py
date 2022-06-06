# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # edge case
        if root is None:
            return 0
        
        # dfs iterative
        stack = []
        # each element will be a list of 2 elements. [depth_of_node, node]. Start with root node with depth 1
        stack.append([1, root])
        # keep a track of max depth
        max_depth = 1
        
        while stack:
            depth, node = stack.pop()
            
            # only process node if it isnt null. Add its left and right children, including null. This if statement will ignore them later
            if node:
                # update max_depth only if this node exists
                max_depth = max(max_depth, depth)
                stack.append([depth+1, node.left])
                stack.append([depth+1, node.right])
            
        return max_depth
        