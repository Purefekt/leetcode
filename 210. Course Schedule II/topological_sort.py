"""
Topological sorting (explanation in Q207)
Just keep a track of all nodes we process in the queue

O(e+v) time
O(e+v) space
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {i:[] for i in range(numCourses)}
        in_edges = {i:0 for i in range(numCourses)}

        for dst, src in prerequisites:
            adj[src].append(dst)
            in_edges[dst] += 1
        
        # add all nodes with 0 in_edges to the queue
        queue = []
        for k,v in in_edges.items():
            if v == 0:
                queue.append(k)
        
        if not queue: return []
        
        res = []
        while queue:
            node = queue.pop()
            res.append(node)

            for child in adj[node]:
                in_edges[child] -= 1
                if in_edges[child] == 0:
                    queue.append(child)
        
        # check if all are 0
        for v in in_edges.values():
            if v > 0:
                return []
        
        return res
        