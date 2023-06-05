"""
Build the tree recursively
Find the midpoint(m) and set that as the root node.
To find left, repeat the same but with the array being [0, m-1]
To find right, repeat the same but with the array being [m+1, len(arr)-1]
Base case is if left index > right index, then this node will be None

O(n) time since we visit each node once
O(logn) space, the recursion stack takes this much space since it is height balanced 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(l,r):
            if l>r:
                return None
            
            m = (l+r)//2
            root = TreeNode(nums[m])
            root.left = helper(l, m-1)
            root.right = helper(m+1, r)

            return root
        
        return helper(0, len(nums)-1)
