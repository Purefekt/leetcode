"""
Give index numbers to each index.
Start with giving the root index = 1.
The left child of a node will have index 2*index.
The right child of a node will have 2*index+1.
This is beacause at each level, the number of nodes increases by 2*index times.
The levels with indexes will be like [1][2,3][4,5,6,7]. Here 6 and 7 are 3's children. Thus the left index is 2*3 and right index is 2*3+1.
Do this with level order bfs and maintain a current level list. The left most will be [0] index and right most will be [-1] index.
Keep track of the max width seen through all levels.

O(n) time for bfs through n nodes.
O(n) space to store cur_level array
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = [(root, 1)]
        res = 1

        while queue:
            cur_level = []
            for i in range(len(queue)):
                node, idx = queue.pop(0)
                cur_level.append(idx)

                if node.left:
                    queue.append((node.left, 2*idx))
                if node.right:
                    queue.append((node.right, 2*idx+1))
                
                l = cur_level[0]
                r = cur_level[-1]
                res = max(res, r-l+1)
        
        return res
