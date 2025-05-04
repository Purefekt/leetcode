"""
Simple level order bfs.
Reverse the result.

O(n) time to go through each node at most once
O(n) space used by queue
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # do top to bottom and reverse
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            res.append(level)
        
        res = res[:-1]
        res = res[::-1]
        return res
