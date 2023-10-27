"""
If any connected component (island) has any cell in the border, then this island cannot be surrounded by 1s.
If all cells of the island are not in border, then it is surrounded by 1s.
Run dfs from each new connected component cell and find all its cells.
If at any point any cell is in the border, then set a flag.
At the end of dfs of a connected component, is flag is False, increment result.

O(m*n) time since we visit a cell at most once, there are m*n cells.
O(m*n) space for stack and to hold visited.
"""

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        # any island which doesnt have any cells on the border must be surrounded by water
        border = set()
        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or i==m-1 or j==n-1:
                    border.add((i,j))
        
        # start dfs from a new connected component and get all its cells. Mark it with a flag if it has cells in border.
        res = 0
        visited = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i,j) not in visited:
                    flag = False
                    # run dfs
                    stack = [(i,j)]
                    while stack:
                        node = stack.pop()
                        if node in visited:
                            continue

                        if node in border:
                            flag = True
                        for d in directions:
                            dest = tuple(map(lambda x,y : x+y, node, d))
                            r,c = dest
                            if 0<=r<m and 0<=c<n and dest not in visited and grid[r][c] == 0:
                                stack.append(dest)
                        visited.add(node)
                    
                    if flag is False:
                        res += 1
        
        return res
