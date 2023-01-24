"""
The first element in preorder is the root of the tree. In [3,9,20,15,7], 3 is the root.
All the nodes to the left of 3 in the 'inorder' traversal belong to the left subtree and all the nodes to the right of 3 belong to the right subtree.
Since inorder is [9,3,15,20,7], [9] is the leftsubtree and [15,20,7] is the right subtree inorder traversals. Using the index of 3, we can get the preorder left and right.
preorder left is [9] and preorder right is [20,15,7].
Pass these values to the recursive call, everytime set root to TreeNode(preorder[0]), find mid in inorder and get the values

O(n) time to go over all nodes
O(n) space, since implicit stack will take O(n) in worst case and O(logn) in best case
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
