"""
BFS level order traversal
Then for the level order list, get the last element from each row to form result
O(n) time to traverse all nodes
O(n) to store all nodes in level order list
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
            return []
        
        # get level order traversal
        queue = [root]
        level_order = []
        
        while queue:
            curr_level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                curr_level.append(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
            level_order.append(curr_level)
        
        res = []
        for level in level_order:
            res.append(level[-1])
        
        return res
                