"""
Modified Dijkstras.
Use a minHeap for BFS instead of a queue.
But instead of adding the total cost till a node to the heap, add the maxmimum height on that path.
Since we do not care about the total cost of a path, instead we care about the max height seen on a given path.
Return as soon as we reach the goal.

O(n^2*logn) time since we traverse the graph using minheap in that time.
O(n^2) space for visited.
"""

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        pq = [(grid[0][0], 0, 0)]
        heapq.heapify(pq)
        visited = set()
        while pq:
            cur_max_height, i, j = heapq.heappop(pq)
            if i==n-1 and j==n-1:
                return cur_max_height
            if (i,j) in visited:
                continue
            for d in directions:
                dest = tuple(map(lambda x,y:x+y, d, (i,j)))
                r,c = dest
                if 0<=r<n and 0<=c<n and dest not in visited:
                    heapq.heappush(pq, (max(cur_max_height, grid[r][c]), r, c))
            visited.add((i,j))
