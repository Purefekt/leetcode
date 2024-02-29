"""
Level order BFS.
Keep a var level to track which level we are at.
And also for each level, create a max_seen var which is set to either 0 for even level and inf for odd level.
This is because the even levels have increasing order and the odd levels have decreasing.

O(n) time for bfs.
O(n) space for the queue.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = [root]
        level = 0
        while queue:
            if level%2 == 0:
                max_seen = 0
            else:
                max_seen = math.inf
            for i in range(len(queue)):
                # even level, all values must be odd, increasing order
                if level%2 == 0:
                    node = queue.pop(0)
                    if node.val%2 != 1:
                        return False
                    if node.val <= max_seen:
                        return False
                    max_seen = node.val
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                # odd level, all values must be even, decreasing order
                else:
                    node = queue.pop(0)
                    if node.val%2 != 0:
                        return False
                    if node.val >= max_seen:
                        return False
                    max_seen = node.val
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
            level += 1
        
        return True
