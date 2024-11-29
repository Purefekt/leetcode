"""
Modified dijkstras.
Observation: If we cannot go right or down from the top left cell, then we cannot have a solution.
But if we can, then we can 'wander' around and always have a solution.
For this we use dijkstras and the distance between edges will be the time taken to go there.
From a node, we can go to another node based on these cases.
If current distance is already >= next cell, then simply increment time by 1 since we have to spend 1s in moving.
Else if current distance < next cell, then we need to wander around.
If the diff between next cell and current distance is odd, then we we can go there at the time of that cell.
Suppose current distance is 10 and next cell value is 13, we wander to another cell in 11 and then come back to current cell at 12 and then go to the target cell at 13.
If the diff between next cell and current distance is even, then we need to add 1 since cant go to this cell exactly when it opens up.
Suppose current distance is 10 and next cell is 14, we wander to another cell in 11, come back in 12 then wander to another cell in 13 then come back in 14 and then go to target cell in 15.

O(m*n*log(m*n)) time. The pq can have m*n items and each pq operations takes log(m*n) time. We do this for all cells m*n.
O(m*n) space taken by min dist and queue.
"""

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        
        # check if we can even start the traversal ie atleast right or bottom cell of start should be <= 1
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        m = len(grid)
        n = len(grid[0])
        
        pq = [(0, (0,0))]
        heapq.heapify(pq)
        visited = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        min_dist = {}
        for i in range(m):
            for j in range(n):
                min_dist[(i,j)] = math.inf

        while pq:
            t, node = heapq.heappop(pq)
            if node in visited:
                continue
            min_dist[node] = min(min_dist[node], t)

            for d in directions:
                dest = tuple(map(lambda x,y: x+y, node, d))
                r,c = dest
                if 0<=r<m and 0<=c<n and dest not in visited:
                    if t >= grid[r][c]:
                        heapq.heappush(pq, (t+1, dest))
                    else:
                        diff = grid[r][c] - t
                        if diff % 2 == 1:
                            heapq.heappush(pq, (grid[r][c], dest))
                        else:
                            heapq.heappush(pq, (grid[r][c]+1, dest))
            
            visited.add(node)
        
        return min_dist[(m-1,n-1)]
