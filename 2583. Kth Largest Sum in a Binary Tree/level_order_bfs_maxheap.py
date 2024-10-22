"""
Level order bfs + maxheap.
Go through all levels and get the sum of each level.
If size of levels < k, return -1.
Add the negatives of all level sums to create maxheap.
Pop k-1 element.
Return top of heap.

O(n + klogn) time since traversing the tree takes n time and popping k-1 elements from heap takes klogn time.
O(n) space used by levels heap.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        # get sums of all levels
        levels = []
        queue = [root]
        while queue:
            this_level = 0
            for i in range(len(queue)):
                node = queue.pop(0)
                this_level += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            levels.append(-this_level)
        
        if k > len(levels):
            return -1
        

        heapq.heapify(levels)
        for _ in range(k-1):
            heapq.heappop(levels)
        return -levels[0]
