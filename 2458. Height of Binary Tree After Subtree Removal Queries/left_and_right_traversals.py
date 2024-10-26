"""
Do dfs (preorder) to get the height of a tree if we remove current node.
For this we will track the maximum height, now when we get to a node, we know that the current max height is what we will have if we remove this node.
Then we will include that node and increase height by 1.
A problem with this approach is we do not know the true max height when looking at the left node since we have not yet explored the right side.
For this we can do another preorder traversal, but this time do a node -> right -> left instead of node -> left -> right and get the same values.
We will keep the max of both traversals as the value for when a node is removed.
Use a hashmap to store the node values since they are unique.
Then use this to get the result array for each query.

O(q+n) time since we have 2 traversals over all nodes of size n and then use q time to create output result.
O(n) space used by stack and max height after removal hashmap.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        max_height_after_removal = {}

        def preorder_left(node, cur_height):
            nonlocal max_height
            if not node:
                return
            
            # if we remove this node, we will have max height as leftover max height
            if node.val not in max_height_after_removal:
                max_height_after_removal[node.val] = 0
            max_height_after_removal[node.val] = max_height

            # update max height to include this node
            max_height = max(max_height, cur_height)

            preorder_left(node.left, cur_height + 1)
            preorder_left(node.right, cur_height + 1)

        def preorder_right(node, cur_height):
            nonlocal max_height
            if not node:
                return
            
            max_height_after_removal[node.val] = max(max_height, max_height_after_removal[node.val])

            max_height = max(max_height, cur_height)

            preorder_right(node.right, cur_height + 1)
            preorder_right(node.left, cur_height + 1)
        

        max_height = 0
        preorder_left(root, 0)
        # reset for second traversal
        max_height = 0
        preorder_right(root, 0)

        res = [max_height_after_removal[q] for q in queries]
        return res
