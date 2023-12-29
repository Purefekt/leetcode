"""
Recursion.
For each node, check if it is a valid node.
Base case return 0 if the node is null.
Recursive function takes (node, maxSeen), initialize with (root, -math.inf) since there can be negative values.
If node.val >= maxSeen, then return sum of left + right + 1 and set maxSeen to node.val since this is the new maxSeen.
If the node.val < maxSeen, then return sum of left + right (we do not add 1 since it is NOT a good node) and maxSeen isnt changed.

O(n) time to go over all nodes at most once.
O(n) space for stack.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def helper(node, maxSeen):

            if not node:
                return 0

            if node.val >= maxSeen:
                return helper(node.left, node.val) + helper(node.right, node.val) + 1
            
            else:
                return helper(node.left, maxSeen) + helper(node.right, maxSeen)
        
        return helper(root, -math.inf)
