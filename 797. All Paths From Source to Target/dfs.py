"""
Create a graph using adj list
run dfs, start the stack with a path, the first path is just the first node [0]
On each iteration, pop the path from the stack. The last element in the path will be the node to expand on
If this node is the destination, then append this valid path to the result.
Else expand this path with its children nodes and all all those paths to the stack

O(2^n *n) time complexity. There can be at max O(2^(n-1)-1) possible paths. Each path takes O(n) time to build a path
O(n2^n *n) space. At a point the stack can contain all paths
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        destination = len(graph)-1

        adj = {}
        for i in range(len(graph)):
            adj[i] = graph[i]
        
        stack = [[0]]
        res = []
        while stack:
            path = stack.pop()
            node = path[-1]

            if node == destination:
                res.append(path)

            else:
                for child in adj[node]:
                    new_path = path[:]
                    new_path.append(child)
                    stack.append(new_path)
            
        return res
            