"""
BFS iterative.
Start queue with (root, root.val). In each iteration check if the current node val >= max val of path
If it is, then increment count by 1
Add left and right children and also add the max val of that path

O(n) time. For n number of nodes, we visit each atleast once
O(n) space to maintain the queue
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count = 0
        if not root:
            return count
        
        queue = [(root, root.val)]

        while queue:
            node, max_val = queue.pop(0)
            if node.val >= max_val:
                count += 1

            if node.left:
                queue.append((node.left, max(max_val, node.left.val)))
            if node.right:
                queue.append((node.right, max(max_val, node.right.val)))
        
        return count
        