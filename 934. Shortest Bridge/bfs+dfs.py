"""
DFS + BFS.
Use DFS to find both the connected components island1 and island2.
Use BFS from island1 to all other cells.
Do level order bfs and add the depth to each cell, only add to a cell once since this will be the min distance to it from island1.
Take the min of distances of all cells which are in island2.

O(n^2) time. n^2 time to run DFS and then n^2 time to run BFS.
O(n^2) time for the stack and queue.
"""

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        # find both the connected components
        visited = set()
        islands = []
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    # run dfs to find this connected component
                    stack = [(i,j)]
                    this_island = []
                    while stack:
                        node = stack.pop()
                        if node in visited:
                            continue
                        this_island.append(node)
                        for d in directions:
                            dest = tuple(map(lambda x,y: x+y, node, d))
                            r,c = dest
                            if 0<=r<n and 0<=c<n and grid[r][c] == 1:
                                stack.append(dest)
                        visited.add(node)
                    islands.append(this_island)
        
        # start bfs from the first island
        # go till the 2nd island
        queue = islands[0]
        visited = set(queue)
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                for d in directions:
                    dest = tuple(map(lambda x,y: x+y, node, d))
                    r,c = dest
                    if 0<=r<n and 0<=c<n and dest not in visited:
                        grid[r][c] = depth
                        queue.append(dest)
                        visited.add(dest)
                visited.add(node)
        
        # get the min distance to any cell in islands2
        res = math.inf
        for r,c in islands[1]:
            res = min(res, grid[r][c])
        
        return res-1
