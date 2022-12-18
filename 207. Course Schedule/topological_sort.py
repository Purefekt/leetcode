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
        