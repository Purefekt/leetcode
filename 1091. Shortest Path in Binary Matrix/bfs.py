"""
"BFS in 8 directions
Check if (0,0) or (n-1,n-1) is not 0, then return -1
Run bfs from (0,0). check all 8 directions and only add if it is a 0. 
Everytime we check a child, add it to visited to avoid checking that cell again
Append the cost at that node and the child node to the queue
Return the cost when we reach (n-1,n-1)"

O(n^2) time to check all cells atleast once
O(n^2) space to store in queue
"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        directions = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        visited = set()

        def valid_child(source, direction):
            destination = tuple(map(lambda x,y:x+y, source, direction))
            r = destination[0]
            c = destination[1]

            if 0 <= r < n and 0 <= c < n:
                if destination not in visited:
                    if grid[r][c] == 0:
                        return destination
            return None 
    

        start = (0,0)
        queue = [(start,1)]
        while queue:
            src, cost = queue.pop(0)

            if src == (n-1,n-1):
                return cost
            
            for direction in directions:
                child = valid_child(src,direction)
                if child:
                    queue.append((child, cost+1))
                visited.add(child)
            
            visited.add(src)
        
        

        return -1