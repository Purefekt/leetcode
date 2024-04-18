class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # for land cells in 0th or m-1th rows, will get +1 for perimeter
                    if i==0:
                        res += 1
                    if i==m-1:
                        res += 1
                    # for land cells in 0th or n-1th cols, will get +1 for perimeter
                    if j==0:
                        res += 1
                    if j==n-1:
                        res += 1

                    # check if it has a neighbor in all 4 directions, for no neighbhor +1 for perimeter
                    if 0<=i+1<m and 0<=j<n and grid[i+1][j] == 0:
                        res += 1
                    if 0<=i<m and 0<=j+1<n and grid[i][j+1] == 0:
                        res += 1
                    if 0<=i-1<m and 0<=j<n and grid[i-1][j] == 0:
                        res += 1
                    if 0<=i<m and 0<=j-1<n and grid[i][j-1] == 0:
                        res += 1
        
        return res
