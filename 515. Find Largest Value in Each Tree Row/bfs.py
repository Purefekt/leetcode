"""
Level order bfs and get the max from each row.

O(n) time to iterate over all nodes and max over all elements.
O(n) space used by stack.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        queue = collections.deque()
        queue.append(root)

        res = []
        while queue:
            lvl = []
            for i in range(len(queue)):
                node = queue.popleft()
                lvl.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(max(lvl))
        
        return res
