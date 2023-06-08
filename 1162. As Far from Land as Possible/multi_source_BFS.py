"""
Multi source bfs
Run bfs from all the 1s, initialize the queue with all the 1s
Track the min distance to water
Only add new water and unvisited nodes

O(n^2) time to go over all nodes in a n*n matrix
O(n^2) space since at any time, the queue might have all cells in memory
"""

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        queue = []
        min_dis = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append(((i,j),0))
                else:
                    min_dis[(i,j)] = math.inf
        
        if len(queue) == m*n or len(queue) == 0:
            return -1
        
        visited = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        while queue:
            node, dis = queue.pop(0)

            if node not in visited:
                for d in directions:
                    dest = tuple(map(lambda x,y: x+y, node, d))
                    r,c = dest
                    if 0<=r<m and 0<=c<n and grid[r][c] == 0:
                        min_dis[dest] = min(min_dis[dest], dis+1)
                        queue.append((dest, dis+1))
            visited.add(node)
        return max(min_dis.values())
