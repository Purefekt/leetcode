"""
Iterate the tree level by level and store in a 2d array.
Reverse the odd rows.
Now iterate the tree level by level and replace all node values with the one in the modified 2d array.

O(n) time where n is number of nodes in the tree for 3 passes in total.
O(n) space used by the 2d array.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # get level order traversal
        levels = []
        queue = collections.deque()

        queue.append(root)
        while queue:
            lvl = []
            for i in range(len(queue)):
                node = queue.popleft()
                lvl.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            levels.append(lvl)
    
        # reverse odd rows
        for i in range(len(levels)):
            if i%2 == 1:
                levels[i] = levels[i][::-1]

        # iterate over the tree and replace values
        lvl = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                node.val = levels[lvl][i]
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            lvl += 1
        
        return root
