"""
DFS and BFS.
Use DFS to traverse the tree to build an undirected graph.
During this also store the details for each node -> left, right, parent. In a hashmap.
Now run bfs from the start node and pass the current path.
Use the relationship hashmap to find out what the relationship to the next node is.

O(n) time for a dfs and a bfs pass over the entire tree of n nodes.
O(n) space used by stack for dfs and queue for bfs.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        # traverse the tree to form a graph. Also track its left, right, parent
        adj = collections.defaultdict(list)
        relations = {}
        stack = [(root, None)]
        while stack:
            node, parent = stack.pop()
            relations[node.val] = {}
            if node.left:
                relations[node.val][node.left.val] = 'L'
                stack.append((node.left, node.val))
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
            if node.right:
                relations[node.val][node.right.val] = 'R'
                stack.append((node.right, node.val))
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
            if parent:
                relations[node.val][parent] = 'U'
        
        # use the undirected graph to get shortest path and track the path
        queue = [(startValue, '')]
        visited = set()
        while queue:
            node, path = queue.pop(0)
            if node == destValue:
                return path
            if node in visited:
                continue
            for child in adj[node]:
                if child not in visited:
                    queue.append((child, path+relations[node][child]))
            visited.add(node)
