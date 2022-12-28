"""
Run level order bfs and update the rooms with the depth
Start the bfs with all the gates

O(m*n) Each room is visited at most once since we mark it as not being INF
O(m*n) for the size of queue 
"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        m = len(rooms)
        n = len(rooms[0])
        INF = 2147483647

        # run level order bfs starting from the gates
        queue = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j))
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                for direction in directions:
                    destination = tuple(map(lambda x,y:x+y, node, direction))
                    r,c = destination

                    if 0<=r<m and 0<=c<n and rooms[r][c] == INF:
                        rooms[r][c] = depth
                        queue.append((r,c))
        