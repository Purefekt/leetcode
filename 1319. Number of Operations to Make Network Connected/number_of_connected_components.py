"""
Firstly we need to check if number of connections >= n-1. This is because we need atleast n-1 edges to connect all n vertices (tree).
Next count the number of connected components, we need num_components - 1 of actions to connect all computers.

O(n) time to find all connected components since we traverse all nodes atleast once.
O(n) space for stack
"""

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        # there needs to be atleast n-1 connections to connect all computers (tree)
        if len(connections) < n-1:
            return -1
        
        # find number of connection components, we need num components - 1 to connect
        adj = collections.defaultdict(list)
        for src, dst in connections:
            adj[src].append(dst)
            adj[dst].append(src)
        
        # run dfs from each node, each new graph is a component
        visited = set()
        num_components = 0
        for i in range(n):
            if i not in visited:
                num_components += 1
                # dfs
                stack = [i]
                while stack:
                    node = stack.pop()
                    for child in adj[node]:
                        if child not in visited:
                            stack.append(child)
                    visited.add(node)
        
        return num_components - 1
