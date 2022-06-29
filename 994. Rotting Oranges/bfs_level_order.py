"""
level order bfs traversal. increment the minute on each level.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        # get num of fresh oranges originally
        num_fresh_oranges_originally = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    num_fresh_oranges_originally += 1
        # if num fresh oranges originally is 0, then return 0
        if num_fresh_oranges_originally == 0:
            return 0
        
        # add all the cells with a rotten orange to a queue
        queue = collections.deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
        # if queue is empty, means no rotten oranges on the grid, return -1
        if not queue:
            return -1
        
        # go over all rotten oranges at a level and add all rotten oranges in the next level. inc minutes at each level
        minutes = -1
        while queue:
            minutes += 1
            
            elements_in_curr_level = len(queue)
            directions = [(-1,0), (0,1), (1,0), (0,-1)]
            for i in range(elements_in_curr_level):
                cell_i, cell_j = queue.popleft()
                # all 4 directions for each cell
                for dirs in directions:
                    new_i = cell_i + dirs[0]
                    new_j = cell_j + dirs[1]
                    # validity
                    if new_i>=0 and new_j>=0 and new_i<rows and new_j<cols and grid[new_i][new_j]==1:
                        grid[new_i][new_j] = 2
                        # add this new rotten orange to the queue
                        queue.append((new_i, new_j))
            
        
        # after the while loop ends, check the grid, if there is any fresh orange left, return -1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        # if for loop ends without return, this means no fresh oranges were left. Return minutes
        return minutes
