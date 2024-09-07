"""
Check if we form the link list from each node.
Convert linked list to an array and pass the index.
Helper function runs dfs. 
Base case 1, if idx == len(linked list), return True, since we found a path.
Base case 2, if not node, return False
Base care 3, if node.val != list[idx], return False since this path is useless.
Return or of left and right nodes since any valid path is accepted.
Repeat this for every node in the tree.

O(n*m) time where n is size of tree and m is size of linked list. Since we have to check upto size of m for each of n nodes.
O(n+m) space since the helper function has call stack m and the main function has call stack size n.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        llist = []
        dummy = head
        while dummy:
            llist.append(dummy.val)
            dummy = dummy.next

        def helper(node, idx):
            if idx == len(llist):
                return True
            if not node:
                return False
            if node.val != llist[idx]:
                return False
            return helper(node.left, idx+1) or helper(node.right, idx+1)
        
        stack = [root]
        while stack:
            node = stack.pop()
            if helper(node, 0) is True:
                return True
            if node:
                stack.append(node.left)
                stack.append(node.right)
        return False
            