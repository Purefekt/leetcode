"""
Dijkstras.
Assume the matrix is a graph and cells are the nodes.
From each cell, to go to a cell that is 1 is distance 1.
And to go to a cell with value 0 is distance 0.
Using dijkstras, we will find the shortest distance from top left to bottom right.
This will be the least number of obstacles to remove.

O(m*n*log(m*n)) time since the pq can have m*n items and each pop and push takes log(m*n) time.
O(m*n) space used by min distance hashmap and the pq.
"""

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        min_dist = {}
        for i in range(m):
            for j in range(n):
                min_dist[(i,j)] = math.inf
        
        pq = [(0, (0,0))]
        heapq.heapify(pq)
        visited = set()
        while pq:
            dis, node = heapq.heappop(pq)
            if node in visited:
                continue
            min_dist[node] = min(min_dist[node], dis)

            for d in directions:
                dest = tuple(map(lambda x,y:x+y, node, d))
                r,c = dest
                if 0<=r<m and 0<=c<n and dest not in visited:
                    if grid[r][c] == 1:
                        heapq.heappush(pq, (dis+1, dest))
                    else:
                        heapq.heappush(pq, (dis, dest))
            visited.add(node)
        
        return min_dist[(m-1, n-1)]
