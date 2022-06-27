"""
Use dfs. After edge cases
Each stack element will contain the current node of the 2 trees
Overwrite the tree1 to build the merged tree

For each stack element, pop it, add and update root1.val
if left nodes for both trees exists, add (tree1.left, tree2.left) to the stack
if tree1.left doesnt exists but tree2.left exists, then take the tree2.left subtree and set it as tree1.left
Repeat for right
Note, if tree1.left exists but tree2.left doesnt exist, then do nothing since tree1 will already have all the nodes
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # edge cases
        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        
        stack = collections.deque()
        stack.append((root1,root2))
        
        while stack:
            tree1, tree2 = stack.pop()
            
            tree1.val = tree1.val + tree2.val
            
            # left
            if tree1.left and tree2.left:
                stack.append((tree1.left, tree2.left))
            if not tree1.left and tree2.left:
                tree1.left = tree2.left
            # right
            if tree1.right and tree2.right:
                stack.append((tree1.right, tree2.right))
            if not tree1.right and tree2.right:
                tree1.right = tree2.right
        
        return root1
        