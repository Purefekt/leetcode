"""
Get the shortest distance from node1 and node2 to each of the other nodes.
Use BFS (but DFS will do the same here since each node has at most one outgoing edge).
Create an array of max distance to any node from either node1 or node2.
The result will be the node with the smallest value in the maximum distance array.

O(n) time to run bfs over the entire graph 2 times.
O(n) space for the queue.
"""

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        # build the graph
        adj = {i:[] for i in range(len(edges))}
        for src, dst in enumerate(edges):
            if dst != -1:
                adj[src].append(dst)
        
        # run bfs from node1 and node2 and calculate the distance to each node.
        def bfs(start_node):
            distances = [math.inf] * len(edges)
            queue = [(start_node,0)]
            visited = set()
            while queue:
                node, dis = queue.pop(0)
                if node not in visited:
                    distances[node] = dis
                    for child in adj[node]:
                        queue.append((child, dis+1))
                    visited.add(node)
            return distances
        
        d_node1 = bfs(node1)
        d_node2 = bfs(node2)

        # get the min of max of the distance from node1 and node2 to each node
        max_distances = []
        for i in range(len(edges)):
            max_distances.append(max(d_node1[i], d_node2[i]))
        
        min_distance = min(max_distances)
        if min_distance == math.inf:
            return -1
        for i in range(len(edges)):
            if max_distances[i] == min_distance:
                return i
