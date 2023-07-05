"""
At each node, we find the max value when that node is in the middle of the path and that nodes left and right children are both part of the path. Track this for every node and return the max from all.
We also need to get the max path sum when that node is a part of the path but the path does not split there, ie only the left or the right child can be the part of the path.
Use a helper recusrive function, if the node is null then return 0. Get the left and right values. Update the result array with the node.val + left + right. But since there are negative numbers, we can choose to not include one or both of the children, thus take max of all 4 cases.
The recurisive function will return the node.val + max(left, right, 0). This is because we are returning the max value when we do not split at this node, we also use 0 to have the ability to skip this node in the path.

O(n) time to go over all nodes atleast once.
O(n) space to store n number of different max values
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = []

        def helper(node):

            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            nodeSum = max(
                node.val,
                left + node.val,
                right + node.val,
                left + right + node.val
            )
            nodePath = max(left, right, 0) + node.val

            res.append(nodeSum)
            return nodePath

        helper(root)
        
        return max(res)
