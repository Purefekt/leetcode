"""
Make an array using inorder traversal which will be sorted in non dec order since it is a BST.
Use 2 pointers to traverse the array once and find such a pair or return false.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # get inorder traversal
        stack = collections.deque()
        inorder = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            inorder.append(curr.val)
            curr = curr.right
        
        print(inorder)
        
        # use two pointers
        l = 0
        r = len(inorder)-1
        
        while (l<r):
            if inorder[l] + inorder[r] == k:
                return True
            if inorder[l] + inorder[r] < k:
                l += 1
            if inorder[l] + inorder[r] > k:
                r -= 1
        
        # if while loop terminates without true, we could not find 2 such nums
        return False
        