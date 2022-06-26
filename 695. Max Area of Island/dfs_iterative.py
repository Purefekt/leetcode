class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        max_island_size = 0
        
        for i in range(rows):
            for j in range(cols):     
                # if we find a landmass, get its 4 directional land masses
                if grid[i][j] == 1:
                    stack = collections.deque()
                    stack.append((i,j))
                    curr_island_size = 0

                    while stack:

                        curr_i, curr_j = stack.pop()
                        # inc island size and change curr island num to 2, to avoid re-adding. Similar to 733 ques
                        grid[curr_i][curr_j] = 2
                        curr_island_size += 1
                        # add 4 directional IF they are valid and IF they have value 1. Also change the newely added points to 2 to avoid re-adding.
                        # up
                        if curr_i-1>=0 and curr_j>=0 and curr_i-1<rows and curr_j<cols and grid[curr_i-1][curr_j] == 1:
                            stack.append((curr_i-1,curr_j))
                            grid[curr_i-1][curr_j] = 2
                        # right
                        if curr_i>=0 and curr_j+1>=0 and curr_i<rows and curr_j+1<cols and grid[curr_i][curr_j+1] == 1:
                            stack.append((curr_i,curr_j+1))
                            grid[curr_i][curr_j+1] = 2
                        # down
                        if curr_i+1>=0 and curr_j>=0 and curr_i+1<rows and curr_j<cols and grid[curr_i+1][curr_j] == 1:
                            stack.append((curr_i+1,curr_j))
                            grid[curr_i+1][curr_j] = 2
                        # left
                        if curr_i>=0 and curr_j-1>=0 and curr_i<rows and curr_j-1<cols and grid[curr_i][curr_j-1] == 1:
                            stack.append((curr_i,curr_j-1))
                            grid[curr_i][curr_j-1] = 2


                    # update max island size
                    max_island_size = max(max_island_size, curr_island_size)
                    # reset curr_island_size
                    curr_island_size = 0
                else:
                    continue
    
        return max_island_size
             