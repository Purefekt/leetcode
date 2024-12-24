"""
Level order bfs to extract each individual row.
Find the number of swaps to make this row sorted.
Sort the row to get expected indexes.
Iterate over the array, if positions are the same, continue.
Else, increase swaps and swap with target index.

O(nlogn) time for sorting each row. Tree traversal takes n time.
O(n) space used by queue and hashmap.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        queue = collections.deque()
        queue.append(root)

        def get_swaps(arr):
            sorted_arr = sorted(arr)
            
            cur_idx = {}
            for i,n in enumerate(arr):
                cur_idx[n] = i
            
            swaps = 0
            for i in range(len(arr)):
                if arr[i] != sorted_arr[i]:
                    swaps += 1

                    cur_pos = cur_idx[sorted_arr[i]]
                    cur_idx[arr[i]] = cur_pos
                    arr[cur_pos] = arr[i]
            return swaps

        res = 0
        while queue:
            lvl = []
            for i in range(len(queue)):
                node = queue.popleft()
                lvl.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            num_swaps = get_swaps(lvl)
            res += num_swaps
        
        return res
