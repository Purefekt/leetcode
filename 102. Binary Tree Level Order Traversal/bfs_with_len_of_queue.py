"""
BFS. Start with a queue and the root.
Start a while loop, Each time run a for loop for the length of the current queue.
Inside the for loop, keep popping and adding all nodes in current queue to a list.
Add that nodes left and right children to the queue.
At the end of for loop, we will have a list of all node values in that level. append this to result and repeat for next level

O(n) time to traverse all nodes
O(n) space to maintain all nodes in the queue
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = [root]
        
        res = []
        while queue:
            
            curr_level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                curr_level.append(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                
            res.append(curr_level)
        
        return res
            