"""
Run bfs with cost element from all 0s.
Set up a queue with all mat positions with a 0. Add it to the queue as ((x,y), 0). The position and cost
Add all these nodes to visited as well
Run bfs on this queue in all 4 directions. For valid children which havnt been visited, overwrite their cost in the mat table as cost+1
Add these child nodes to the queue with (pos, cost+1) and add to visited

O(m*n) to traverse all cells to build the queue. Running bfs will also go through all nodes once
O(m*n) to store upto n nodes at max in the queue
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])

        # run bfs from 0s to all 1s
        queue = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append(((i,j),0))
                    visited.add((i,j))
        

        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        while queue:
            node, cost = queue.pop(0)
            r,c = node[0], node[1]
            # check all directions
            for direction in directions:
                destination = tuple(map(lambda x,y:x+y, node, direction))
                new_r, new_c = destination[0], destination[1]

                if 0<=new_r<m and 0<=new_c<n and destination not in visited:
                    visited.add(destination)
                    mat[new_r][new_c] = cost+1
                    queue.append(((new_r, new_c), cost+1))
        
        return mat
                