"""
RUn dfs from the root. Each time add these to the stack -> (path, node, current_sum)
The path is a list of int vals.
If the node is a leaf node and current sum is the target, add this path to the result
Else if left node exists, apprend its val to the path and add to the stack. Same with if right exists

O(n^2) time. We have n nodes in tree. In the worst case we have a complete binary tree, each leaf can have all nodes in valid path, hence O(n) to copy per leaf nodes and we have n/2 leaf nodes 
O(n) space to store the nodes on a given path
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return []


        start_val = root.val
        stack = []
        stack.append(([root.val], root, root.val))
        res = []
        while stack:
            path, node, cur_sum = stack.pop()
            if not node.left and not node.right and cur_sum == targetSum:
                res.append(path)
            
            else:
                if node.left:
                    new_path = path.copy()
                    new_path.append(node.left.val)
                    stack.append((new_path, node.left, cur_sum + node.left.val))
                if node.right:
                    new_path = path.copy()
                    new_path.append(node.right.val)
                    stack.append((new_path, node.right, cur_sum + node.right.val))

        return res
        