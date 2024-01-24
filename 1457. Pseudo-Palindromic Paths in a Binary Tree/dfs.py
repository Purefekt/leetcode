"""
Get all paths to all leaves using dfs.
When we reach the leaf, we need to check if the current path makes a palindrome.
We can check this using frequencies. For a valid palindrome permutation, there can be at mast 1 value which occurs an odd number of times.
[1,1,2,2,3], this is valid since only 3 occurs odd times and the other occur even times. [1,1,2,2,3,4] is invalid.
Iterate down all paths and maintain a frequency hashmap.
At each leaf, iterate the hashmap from 1->9 and see the number of off frequencies, when it exceeds 1, return False.

O(n) time to visit all nodes at most once.
O(n) space for the stack.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        def valid(counter):
            odd_counter = 0
            for i in range(1, 10):
                if counter[i] % 2 == 1:
                    odd_counter += 1
                    if odd_counter > 1:
                        return False
            return True
        
        res = 0

        def dfs(node, freq):

            nonlocal res

            if not node.left and not node.right:
                if valid(freq) is True:
                    res += 1
            
            if node.left:
                freq[node.left.val] += 1
                dfs(node.left, freq)
                freq[node.left.val] -= 1
            
            if node.right:
                freq[node.right.val] += 1
                dfs(node.right, freq)
                freq[node.right.val] -= 1


        freq = {i:0 for i in range(1, 10)}
        freq[root.val] += 1
        dfs(root, freq)

        return res
