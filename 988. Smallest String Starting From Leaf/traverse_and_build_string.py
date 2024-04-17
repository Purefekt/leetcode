"""
Recursively traverse the tree.
Keep building the string using chr().
When we hit a leaf, reverse the string and check it against the current result.
Update it to be min(res, string).

O(n^2) time to traverse all nodes once and each time we concatonate the string which is a linear time operations.
O(n^2) space since the recursive call stack height can be at max n and it stores a string of size n at each time.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        res = None
        def helper(node, s):
            nonlocal res

            if not node:
                return
            
            s += chr(ord('a') + node.val)

            if not node.left and not node.right:
                # we have reached a leaf node
                s = s[::-1]
                if not res:
                    res = s
                else:
                    res = min(res, s)
                return
            
            helper(node.left, s)
            helper(node.right, s)
            s = s[:-1]
        
        helper(root, "")
        return res
