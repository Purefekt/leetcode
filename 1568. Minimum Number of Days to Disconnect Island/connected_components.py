"""
First check if the graph contains 1 component.
If it does not ie no island = 0 components or disconnected ie > 1 component, return 0. Since it is already disconnected.
Now try to flip each land to water one by one and see if doing this operation makes it disconnected.
If it does, then return 1.
In all other cases, return 2, since we can always disconnect a single island with just 2 flips. see below example
[1,1,1,1]       [1,0,1,1]
[1,1,1,1] ==>   [0,1,1,1]
[1,1,1,1]       [1,1,1,1]


O((m*n)^2) time since is_disconnected function runs in m*n time and we run it for potentially all m*n cells.
O(m*n) space used by visited.
"""

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        # check if the graph is already disconnected
        def is_disconnected(matrix):
            
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            components = 0
            visited = set()
            for i in range(m):
                for j in range(n):
                    if (i,j) not in visited and matrix[i][j] == 1:
                        components += 1
                        if components > 1:
                            return True
                        stack = [(i,j)]
                        while stack:
                            node = stack.pop()
                            if node in visited:
                                continue
                            for d in directions:
                                dest = tuple(map(lambda x,y: x+y, node, d))
                                r,c = dest
                                if 0<=r<m and 0<=c<n and dest not in visited and matrix[r][c] == 1:
                                    stack.append(dest)
                            visited.add(node)
            
            if components == 1:
                return False
            return True
        
        # already disconnected
        if is_disconnected(grid) is True:
            return 0
        
        # try to flip each land to water one by one and see if flipping a single land to water makes it disconnected
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if is_disconnected(grid) is True:
                        return 1
                    grid[i][j] = 1 # backtrack
        
        # in all other cases, we can disconnect it within 2 flips
        return 2
