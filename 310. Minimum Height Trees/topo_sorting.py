"""
Topological sorting to find the centroids.
Given the conditions that it is a tree ie there are no cycles and all nodes are connected.
Such a graph will have at most 2 centroids.
We need to remove the leaf nodes level by level and stop when we have reached 2 nodes, it can be 1 also.
Create an adj list for an undirected graph.
Add all current leaf nodes to a queue, ie all nodes with 1 child.
Loop till len(adj) > 2.
Do level order bfs, iterate for the size of the queue, get the only neighbor of current node and remove the connection between this neighbor and current node in the adj[neighbor].
Then remove this key from adj.
If we end up creating a new leaf, ie len(adj[neighbor]) == 1, add it to the queue.
Return the keys which remain in the adj list, there will be either 1 or 2.

O(n) where n is the number of nodes, since there are always n-1 edges. BFS will take v+e.
O(n) space for the queue.
"""

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = {i:set() for i in range(n)}
        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        queue = []
        for k,v in adj.items():
            if len(v) == 1:
                queue.append(k)
        
        while len(adj) > 2:
            for i in range(len(queue)):
                node = queue.pop(0)
                # get the only neighbor of this node
                connected = adj[node].pop()
                # remove this edge
                adj[connected].remove(node)
                del adj[node]
                if len(adj[connected]) == 1:
                    queue.append(connected)
        
        return list(adj.keys())
