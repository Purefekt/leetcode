"""
Go over all cells in the matrix. As soon as we get to 1(land) trigger DFS and find all 1s in that island.
Maintain a visited list to avoid checking those cells again.
For each DFS, add 1 to count

O(m*n) time to traverse all cells in the matrix
O(m*n) space where all are 1s
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        visited = set()
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    count += 1
                    visited.add((i,j))
                    curr_island = [(i,j)]
                    while curr_island:
                        r,c = curr_island.pop()
                        
                        # check top, left, right, down
                        if c-1 >=0 and (r,c-1) not in visited and grid[r][c-1] == '1':
                            curr_island.append((r,c-1))
                            visited.add((r,c-1))
                        if r-1 >=0 and (r-1,c) not in visited and grid[r-1][c] == '1':
                            curr_island.append((r-1,c))
                            visited.add((r-1,c))
                        if c+1 < n and (r,c+1) not in visited and grid[r][c+1] == '1':
                            curr_island.append((r,c+1))
                            visited.add((r,c+1))
                        if r+1 < m and (r+1,c) not in visited and grid[r+1][c] == '1':
                            curr_island.append((r+1,c))
                            visited.add((r+1,c))
                else:
                    continue
        
        return count
                            