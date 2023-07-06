"""
Run level order BFS but always add the RIGHT child first.
Do not keep a track of levels, since adding the right child first means that when we start a level, the node popped the first time is the right most.
So for each level, add the first node to result

O(n) time to run bfs on the entire tree and visit all nodes once.
O(n) space to store the queue
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return
        
        queue = [root]
        res = []
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if i == 0:
                    res.append(node.val)
                
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return res
                    