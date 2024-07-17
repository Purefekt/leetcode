"""
Use a helper function which takes the node and its parent.
If a node.val is not in to_delete and its parent is None, this is the start of a new tree, add this node to res.
Now for each node, pass its left and right children nodes and itself as parent.
But if this node itself is to be deleted, pass None as parent to indicate that the next node (child) will be the start of a tree.
Also if a child of a node is to be deleted, then set the node.side to None to remove it from that tree.

O(n) time to go over all nodes once.
O(n) space used by stack.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        to_delete = set(to_delete)
        res = []
        def helper(node, parent):
            if not node:
                return

            if not parent and node.val not in to_delete:
                res.append(node)
            
            parent = node
            if node.val in to_delete:
                parent = None
            
            if node.left:
                helper(node.left, parent)
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                helper(node.right, parent)
                if node.right.val in to_delete:
                    node.right = None
        
        helper(root, None)
        return res
