"""
BFS to find number of components
Initialize the bidirectional adj list
Go over all the nodes in the adj list, if it hasnt been in visited then increment count by 1
Start bfs at every node being checked to get rid of more nodes

O(e+v) time
O(e+v) space
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i:[] for i in range(n)}
        for src,dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        parents = [i for i in range(n)]

        visited = set()
        count = 0

        for root in adj.keys():
            if root not in visited:
                count += 1

                # run bfs and mark all nodes from this and continue
                queue = [root]
                while queue:
                    node = queue.pop(0)
                    for child in adj[node]:
                        if child not in visited:
                            visited.add(child)
                            queue.append(child)
                    visited.add(node)
        
        return count
