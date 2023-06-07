"""
Level order traversal
Save all levels, the result will be the first element of the last level

O(n) time to traverse all nodes
O(n) space to store all nodes
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        # level order traversal
        levels = []

        queue = [root]
        while queue:
            this_level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                this_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(this_level)
        
        return levels[-1][0]
        