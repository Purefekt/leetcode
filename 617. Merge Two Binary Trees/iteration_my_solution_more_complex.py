"""
Use dfs and check each node and overwrite on tree2.
After the edge cases, each stack element will have 4 elements = [node_tree1, node_tree2, parent, direction]

If the node exists in both trees, then simply change the val of tree2 node to tree1.val + tree2.val. Then append left and right nodes with all 4 data points to the stack
If node doesnt exist in tree1 but exists in tree2 then do nothing, since we are building on tree2
If node exists on tree1 but not on tree2, then based on if its a left or right direction node, copy that node to the parents left or right
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
        stack.append((root1,root2, root2, None))
        
        while stack:
            tree1, tree2, parent, direction = stack.pop()
            if tree1 and tree2:
                tree2.val = tree1.val + tree2.val
                stack.append((tree1.left, tree2.left, tree2, 'l'))
                stack.append((tree1.right, tree2.right, tree2, 'r'))
            
            if not tree1 and tree2:
                continue
            
            if tree1 and not tree2:
                if direction == 'l':
                    parent.left = tree1
                elif direction == 'r':
                    parent.right = tree1
        
        return root2
        