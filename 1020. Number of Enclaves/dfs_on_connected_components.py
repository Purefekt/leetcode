"""
Get a set of all nodes in the border.
Run dfs for each connected component, use a visited set to start dfs on a brand new component.
For each node being added to the component, if it belongs to the border set, then set it a flag to True.
After dfs for a component is done, if the flag is false, all the nodes of this component cannot reach the border, add count to result.

O(m*n) since we will traverse a cell at most once.
O(m*n) space for stack which can grow to at max size m*n.
"""

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        border = set()

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    border.add((i,j))
            
        visited = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    # start DFS
                    flag = False
                    nodes_in_group = 0
                    stack = [(i,j)]
                    while stack:
                        node = stack.pop()
                        if node in visited:
                            continue
                        nodes_in_group += 1
                        if node in border:
                            flag = True
                        for d in directions:
                            dest = tuple(map(lambda x,y: x + y, node, d))
                            r,c = dest
                            if 0<=r<m and 0<=c<n and dest not in visited and grid[r][c] == 1:
                                stack.append(dest)
                        visited.add(node)
                    if flag is False:
                        res += nodes_in_group
        
        return res
