"""
Go through all cells in the matrix
Run DFS everytime we are at a cell with 1 and get max size
Use visited set to avoid going to cells again
O(m*n) time to iterate over all cells
O(m*n) space to store all cells
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        visited = set()
        max_size = 0
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    curr_island_size = 0
                    
                    stack = [(i,j)]
                    visited.add((i,j))
                    while stack:
                        r,c = stack.pop()
                        curr_island_size += 1
                        
                        # check and add all directions
                        if r-1>=0 and grid[r-1][c] == 1 and (r-1,c) not in visited:
                            stack.append((r-1,c))
                            visited.add((r-1,c))
                        if c+1<n and grid[r][c+1] == 1 and (r,c+1) not in visited:
                            stack.append((r,c+1))
                            visited.add((r,c+1))
                        if r+1<m and grid[r+1][c] == 1 and (r+1,c) not in visited:
                            stack.append((r+1,c))
                            visited.add((r+1,c))
                        if c-1>=0 and grid[r][c-1] == 1 and (r,c-1) not in visited:
                            stack.append((r,c-1))
                            visited.add((r,c-1))
                        
                    max_size = max(max_size, curr_island_size)
                
                else:
                    continue
        
        return max_size
                        