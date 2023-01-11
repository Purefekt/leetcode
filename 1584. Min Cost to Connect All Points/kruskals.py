"""
Kruskals algo, Minimum spanning tree
We first build a list of all edges (manhattan dist b/w points), we also encode the source and destination into this list, we can have at most n^2 edges
We then convert this to a minheap using heapify in linear time
Run a while loop till we get n-1 valid edges, an edge is valid if it doesnt cause a cycle in the graph
Using a minheap we are able to get the smallest edge

O(n^2logn) time. O(n^2) for max number of egdes and O(logn) for minheappop
O(n^2) space to store all edges
"""

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan_dist(point_a, point_b):
            x_i, y_i = point_a
            x_j, y_j = point_b
            return abs(abs(x_i - x_j) + abs(y_i - y_j))

        # get manhannatan distance b/w all points ie, get all edges and their weights
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append((manhattan_dist(points[i], points[j]), tuple(points[i]), tuple(points[j])))
        
        # heapify runs in O(n), better than sorting list or building heap one by one
        heapq.heapify(edges)

        # build the adj list
        adj = {tuple(point):[] for point in points}

        def detect_cycle_dfs(start):
            visited = set()
            stack = [start]
            while stack:
                node = stack.pop()
                if node in visited:
                    return True
                for child in adj[node]:
                    if child not in visited:
                        stack.append(child)
                visited.add(node)
            return False
        
        res = 0
        count = 0
        while count != len(points)-1:

            edge, src, dst = heapq.heappop(edges)

            # add to adj list
            adj[src].append(dst)
            adj[dst].append(src)

            # check if there is no cycle
            if detect_cycle_dfs(src) is True:
                adj[src].pop()
                adj[dst].pop()
            else:
                res += edge
                count += 1
        
        return res
        