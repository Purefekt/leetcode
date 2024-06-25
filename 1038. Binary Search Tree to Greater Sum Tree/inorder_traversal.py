"""
Inorder traversal.
Get the inorder traversal of the tree, this gives all nodes in increasing order.
Calculate the reverse prefixsum, this will be the sum of all nodes + itself which are greater than node.
Use a hashmap to assign a node value to its new value, since all node values are unique.
Traverse the tree again and use the hashmap to assign new values.

O(n) time for 4 passes over all nodes.
O(n) space used by inorder traversal list, psum list and hashmap.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # get inorder traversal
        inorder_trav = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inorder_trav.append(node.val)
            inorder(node.right)
        
        inorder(root)

        # get reverse psum
        rev_psum = [0] * len(inorder_trav)
        cur = 0
        for i in range(len(inorder_trav)-1, -1, -1):
            cur += inorder_trav[i]
            rev_psum[i] = cur
        
        # map node value to its supposed value
        hashmap = {}
        for i in range(len(inorder_trav)):
            hashmap[inorder_trav[i]] = rev_psum[i]
        
        # replace these values in the bst 
        def dfs(node):
            if not node:
                return
            
            node.val = hashmap[node.val]
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return root
