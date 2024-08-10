"""
Convert to a graph problem.
Each cell in the matrix can potentially be 2 nodes of a graph if the cell has either / or \.
For /, a cell has an 'up' node which can travel to top and left node.
For /, a cell has a 'down' node which can travel to bottom and right node.
For \, a cell has an 'up' node which can travel to top and right node.
For \, a cell has a 'down' node which can travel to left and down node.
For ' ', this cell can travel in all 4 directions
Set a node with ' ' to (r,c).
Set the top half of a node with '/' or '\\' as (r,c,'u') and the bottom half as (r,c,'d')
There are rules to follow when deciding the child node as well.
When entering a child from bottom to top ie moving up from current node, we always enter the down half.
When entering a child from left to right ie moving right from current node, we enter '\\' at the down node and '/' at the up node.
Similar rules for moving down and left as well.
Once graph is created, run simple dfs connected components algorithm to get the solution.

O(n^2) time since we traverse the graph at most 3n^n times.
O(n^2) space used by stack.
"""

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        n = len(grid)

        # return which cell is the child of making this move
        def go_up(r,c):
            if grid[r][c] == ' ':
                return (r,c)
            elif grid[r][c] == '\\':
                return (r, c, 'd')
            elif grid[r][c] == '/':
                return (r, c, 'd')
        
        def go_right(r,c):
            if grid[r][c] == ' ':
                return (r,c)
            elif grid[r][c] == '\\':
                return (r, c, 'd')
            elif grid[r][c] == '/':
                return (r,c,'u')
        
        def go_down(r,c):
            if grid[r][c] == ' ':
                return (r,c)
            elif grid[r][c] == '\\':
                return (r,c,'u')
            elif grid[r][c] == '/':
                return (r,c,'u')

        def go_left(r,c):
            if grid[r][c] == ' ':
                return (r,c)
            elif grid[r][c] == '\\':
                return (r,c,'u')
            elif grid[r][c] == '/':
                return (r,c,'d')
        
        # build graph
        adj = {}
        for i in range(n):
            for j in range(n):
                # '' goes in all 4 directions
                if grid[i][j] == ' ':
                    node = (i,j)
                    adj[node] = []
                    # go up
                    if i-1 >= 0:
                        child = go_up(i-1,j)
                        adj[node].append(child)
                    # go right
                    if j+1 < n:
                        child = go_right(i,j+1)
                        adj[node].append(child)
                    # go down
                    if i+1 < n:
                        child = go_down(i+1,j)
                        adj[node].append(child)
                    # go left
                    if j-1 >= 0:
                        child = go_left(i, j-1)
                        adj[node].append(child)

                # \ creates 2 nodes, up goes up and right. down goes down and left
                elif grid[i][j] == '\\':
                    node_u = (i,j,'u')
                    adj[node_u] = []
                    # go up
                    if i-1 >= 0:
                        child = go_up(i-1, j)
                        adj[node_u].append(child)
                    # go right
                    if j+1 < n:
                        child = go_right(i,j+1)
                        adj[node_u].append(child)
                    
                    node_d = (i,j,'d')
                    adj[node_d] = []
                    # go_down
                    if i+1 < n:
                        child = go_down(i+1, j)
                        adj[node_d].append(child)
                    # go left
                    if j-1 >= 0:
                        child = go_left(i, j-1)
                        adj[node_d].append(child)
                
                # / creates 2 nodes, up goes left and up. down goes right and down.
                elif grid[i][j] == '/':
                    node_u = (i,j,'u')
                    adj[node_u] = []
                    # go up
                    if i-1 >= 0:
                        child = go_up(i-1, j)
                        adj[node_u].append(child)
                    # go left
                    if j-1 >= 0:
                        child = go_left(i, j-1)
                        adj[node_u].append(child)
                    
                    node_d = (i,j,'d')
                    adj[node_d] = []
                    # go right
                    if j+1 < n:
                        child = go_right(i, j+1)
                        adj[node_d].append(child)
                    # go down
                    if i+1 < n:
                        child = go_down(i+1, j)
                        adj[node_d].append(child)

        # run connected components algorithm on this graph
        res = 0
        visited = set()
        for start in adj:
            if start not in visited:
                res += 1
                stack = [start]
                while stack:
                    node = stack.pop()
                    if node in visited:
                        continue
                    for child in adj[node]:
                        if child not in visited:
                            stack.append(child)
                    visited.add(node)
        
        return res
