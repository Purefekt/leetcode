"""
Topological sorting.
Create a adj list and a hashmap of in_edges for each node
For all nodes with initial in_edges as 0, add it to the queue. (if the queue is empty return False since no topological ordering found)
GO through the queue, for each node reduce its children's in_edge count by 1. If any child's in_edge count becomes 0, add it to the queue
Once the queue is empty, check the in_edges for all nodes, if there is even one node with >0 then return False, else True

O(e+v) time. 
O(v+e) space
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(numCourses)}
        in_edges = {i:0 for i in range(numCourses)}

        for src, dst in prerequisites:
            adj[src].append(dst)
            in_edges[dst] += 1
        
        # add all nodes with 0 in_edges to the queue
        queue = []
        for k,v in in_edges.items():
            if v==0:
                queue.append(k)
        
        if not queue: return False
        
        while queue:
            node = queue.pop(0)
            # reduce in edges of all nodes this leads to
            for child in adj[node]:
                in_edges[child] -= 1
                if in_edges[child] == 0:
                    queue.append(child)
        
        # check all nodes, if all are 0 then return True
        for v in in_edges.values():
            if v > 0:
                return False
        return True
        