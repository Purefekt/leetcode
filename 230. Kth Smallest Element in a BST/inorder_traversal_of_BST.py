"""
Get the inorder traversal of the BST. Inorder traversal of the BST will print all nodes in ascending order.
The kth smallest element will be the k-1st index of the inorder traversal

O(n) time to go over all nodes
O(n) space to store all nodes in inorder traversal array
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        inorder_traversal = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            inorder_traversal.append(node.val)
            inorder(node.right)
        
        inorder(root)

        return inorder_traversal[k-1]
        