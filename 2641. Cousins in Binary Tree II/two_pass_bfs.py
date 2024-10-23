"""
One pass level order bfs to get sums of each level.
Another pass where we get the sum of children of each node and then assign the children next level sum - children sum.

O(n) time to go over all nodes twice.
O(n) space used by levels to hold all the totals and the queue.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # get the sums of each level
        levels = []
        queue = [root]
        while queue:
            total = 0
            for i in range(len(queue)):
                node = queue.pop(0)
                if not node:
                    continue
                total += node.val
                queue.append(node.left)
                queue.append(node.right)
            levels.append(total)
        
        root.val = 0
        queue = [root]
        depth = 1
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                children_total = 0
                if node.left: children_total += node.left.val
                if node.right: children_total += node.right.val
                if node.left:
                    node.left.val = levels[depth] - children_total
                    queue.append(node.left)
                if node.right:
                    node.right.val = levels[depth] - children_total
                    queue.append(node.right)
            depth += 1
        
        return root
