"""
Sort the logs
Iterate through the logs, for each time, add to the adj list and run bfs.
Count the number of nodes, if it equals n, return the time
If we go through all logs and the number of nodes in the last bfs is also not n, return -1

O(m(n+e) + mlogm) time. O(n) time to setup adj list. O(m) time to iterate though all logs and O(n+e) time to run bfs on it in nested loop. O(mlogm) to sort.
O(n+e) to store n nodes as keys and e edges as values. n nodes to store in visited.
"""

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        adj = {i:[] for i in range(n)}
        
        def find_num_nodes():
            queue = [0]
            num_nodes = 0
            visited = set()
            while queue:
                node = queue.pop(0)
                num_nodes += 1
                for child in adj[node]:
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
                visited.add(node)
            return num_nodes
                
        
        logs.sort()
        for time, src, dst in logs:
            adj[src].append(dst)
            adj[dst].append(src)

            # run bfs and see if we traverse all nodes
            num_nodes_in_graph = find_num_nodes()
            if num_nodes_in_graph == n:
                return time
        
        return -1
