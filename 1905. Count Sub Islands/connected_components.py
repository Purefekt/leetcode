"""
Connected components from grid2.
Start connected component algo with dfs from all valid start cells in grid2.
During this process, keep a flag. 
This flag stays true if ALL cells being searched in that component of grid2 are 1 in grid1.
At the end of a connected component search, if flag is True, this means this component is a sub graph in grid1.

O(m*n) time since we explore each cell at most once due to visited set.
O(m*n) space used by stack and visited set.
"""

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        m = len(grid1)
        n = len(grid1[0])

        res = 0
        visited = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i,j) not in visited:
                    # get this connected component in grid2 and also check if all these cells are 1 in grid1
                    stack = [(i,j)]
                    valid = True if grid1[i][j] == 1 else False
                    while stack:
                        node = stack.pop()
                        if node in visited:
                            continue
                        for d in directions:
                            dest = tuple(map(lambda x,y: x+y, node, d))
                            r,c = dest
                            if 0<=r<m and 0<=c<n and dest not in visited and grid2[r][c] == 1:
                                if grid1[r][c] == 0:
                                    valid = False
                                stack.append(dest)
                        visited.add(node)
                    # if valid, increment res since this is a subgraph
                    if valid:
                        res += 1
        
        return res
