"""
Run DFS for each time from 0 till n^2.
Optimize by triggering DFS only when both start and end are <= t.
Return the very first time a valid path from start to stop exists.

O(n^4) since we run dfs which takes O(n^2) each time for t which ranges till n^2. The cost is amortized since we only go to all n^2 nodes at most once in the dfs when all nodes are unlocked.
O(n^2) space for stack and visited.
"""

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        for t in range(n**2):
                    
            # run dfs to find a possible path, only start if both [0,0] and [n-1,n-1] are open
            if grid[0][0] <= t and grid[n-1][n-1] <= t:
                visited = set()
                stack = [(0,0)]
                while stack:
                    node = stack.pop()
                    if node == (n-1,n-1):
                        return t
                    if node in visited:
                        continue
                    for d in directions:
                        dest = tuple(map(lambda x,y:x+y, d, node))
                        r,c = dest
                        if 0<=r<n and 0<=c<n and dest not in visited and grid[r][c] <= t:
                            stack.append(dest)
                    visited.add(node)
                    