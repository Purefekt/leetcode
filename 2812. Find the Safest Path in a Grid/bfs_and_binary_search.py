"""
Python code is asymptotically correct but fails.
Run bfs from a queue of all the thieve locations to get the min manhattan distance of each point.
Then set l to 0 and r to max manhatten distance found.
Run binary search on this space.
For each pivot, discard all cells which have distance < pivot.
If there exists a path between (0,0) and (n-1,n-1) this means this is a valid pivot and shift l=p+1.
Else shift r=p-1.

O(n^2*logn) time. 
O(n^2) space.
"""

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        dis = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(math.inf)
            dis.append(row)

        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([(i,j), 0])
    
        # run bfs from each thiev to get all distances. Also get max depth to set as r for binary search
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        while queue:
            node, depth = queue.pop(0)
            i,j = node
            if node in visited:
                continue
            dis[i][j] = depth
            for mov in moves:
                dest = tuple(map(lambda x,y: x+y, node, mov))
                r,c = dest
                if 0<=r<m and 0<=c<n and dest not in visited:
                    queue.append([dest, depth+1])
            visited.add(node)
        
        l = 0
        r = 0
        for row in dis:
            r = max(r, max(row))
        
        def dfs(pivot):
            stack = [(0,0)]
            visited = set()
            while stack:
                i,j = stack.pop(0)
                if (i,j) in visited or dis[i][j] < pivot:
                    continue
                if i==m-1 and j==n-1:
                    return True
                for mov in moves:
                    dest = tuple(map(lambda x,y:x+y, (i,j), mov))
                    r,c = dest
                    if 0<=r<m and 0<=c<n and dest not in visited and dis[r][c] >= pivot:
                        stack.append(dest)
                visited.add((i,j))
            return False
        
        # run binary search on the possible space. For each pivot, consider all cells <pivot to be unusable. If there exists a path from (0,0) to (n-1,n-1) then this is the best we currently can do and we move l=p+1
        res = 0
        print(l,r)
        while l<=r:
            p = (l+r)//2
            if dfs(p) is True:
                res = p
                l = p+1
            else:
                r = p-1
        
        return res
