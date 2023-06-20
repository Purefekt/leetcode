"""
Use BFS for level order traversal.
If we come across a single None, then we are not allowed to encounter any nodes.
Maintain a flag, with initial value False. Set it to True on the first encounter of None node.
Continue BFS, if a node is not None but flag is True, this means it is not a complete binary tree.

O(n) time to go over all nodes once.
O(n) space for the queue.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = [root]
        flag = False

        while queue:
            node = queue.pop(0)

            if flag is True and node is not None:
                return False
            
            if node is None:
                flag = True
            
            if node:
                queue.append(node.left)
                queue.append(node.right)
        
        return True
