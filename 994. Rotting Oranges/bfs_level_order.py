"""
Run bfs level order.
Get the 2s in the original grid and run bfs and keep adding in 4 directions
Increment the time only at every level.
Add edge cases for when there are no rotting oranges but some fresh oranges or if there are no fresh oranges

O(m*n) time to go through all cells once since we add it to seen
O(m*n) to store in queue
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        # create initial queue with all rotten oranges. Also maintain a set of coords of all 1s
        queue = []
        fresh_oranges = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_oranges.add((i,j))
        
        # if the queue is empty and fresh_oranges is not, this means there are only fresh oranges, return -1
        if not queue and fresh_oranges:
            return -1
        # if fresh_oranges is empty, this means time taken is 0
        if not fresh_oranges:
            return 0
        
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        time = -1
        seen = set()
        while queue:
            time += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                seen.add(node)
                for direction in directions:
                    destination = tuple(map(lambda x,y:x+y, node, direction))
                    new_r, new_c = destination[0], destination[1]
                    if 0<=new_r<m and 0<=new_c<n:
                        if destination not in seen:
                            seen.add(destination)
                            if grid[new_r][new_c] == 1:
                                queue.append(destination)
                                grid[new_r][new_c] = 2
        
        # go through the grid, if it still has any 1, this means all oranges were not affected
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return time
        