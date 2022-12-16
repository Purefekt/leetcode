"""
Create adj list and run bfs
Run bfs for every single node. Only increase the count if we actually need to run a bfs, ie if it is not in visited

O(n^2) to build the adj list, need to traverse all points in matrix
O(n) to store the nodes in visited set
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)

        adj = {i:[] for i in range(n)}
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    if isConnected[i][j] == 1:
                        adj[i].append(j)
        
        num_provinces = 0
        visited = set()
        for city in adj.keys():

            if city not in visited:
                num_provinces += 1

                # run bfs from this province
                queue = [city]
                while queue:
                    cur_city = queue.pop(0)
                    for child in adj[cur_city]:
                        if child not in visited:
                            visited.add(child)
                            queue.append(child)
                    visited.add(cur_city)
        
        return num_provinces
