"""
run bfs and see if we hit all nodes
if not then there are more than 1 components -> False.
If a single component then see if the number of edges is n-1, else False.

O(n+e) time. O(n) time to add all n nodes to the adj list and O(e) time to add all edges. Running bfs is also O(n+e)
O(n+e) space. adj list keys if of length n and the inner lists are of length e for all edges. In the worst case the queue will have n nodes in it.
""" 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(n)}
        for src,dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        # bfs
        num_nodes = 1
        visited = set()
        queue = [0]
        while queue:
            node = queue.pop(0)
            for child in adj[node]:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)
                    num_nodes += 1
            visited.add(node)
        
        if num_nodes != n:
            return False
        
        if len(edges) != n-1:
            return False
        
        return True
