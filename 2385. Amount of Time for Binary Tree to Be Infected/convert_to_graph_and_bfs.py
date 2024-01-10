"""
Convert the tree into an undirected graph.
Run level order bfs from the start node.
Return max level.

O(n) time. One pass to go through the tree and build the adj list. Another pass to run level order bfs.
O(n) space. n space for adj list and n space for queue and visited.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        adj = collections.defaultdict(list)

        stack = [root]
        while stack:
            node = stack.pop()

            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
                stack.append(node.left)
            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
                stack.append(node.right)
        
        # run level order bfs from start
        visited = set()
        queue = [start]
        res = 0
        while queue:
            res += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                
                if node in visited:
                    continue
                
                for child in adj[node]:
                    if child not in visited:
                        queue.append(child)
                
                visited.add(node)
        
        return res-1
