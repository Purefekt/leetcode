"""
Run DFS starting from each cell which is not 0. Can move in 4 directions and also when it is not 0
Backtracking using iterations, in the stack store the node, a set of visited nodes in that path, the gold in that path
Keep a global variable max gold and update it
For each dfs return the max gold for that node and also the number of cells for that path, this is to avoid running dfs on every cell if we aready explored 25 cells since the contraint says at max 25 cells will have gold
Check if the num of cells in the path is >= 24, if yes then simply return max gold cos we have explored every single cell which has gold on the entire grid

O(k*3^k) time. We have k cells with gold in them (k is at max 25). Each dfs we start with a cell which can go to 4 neighbhors but from every next point it has 3 places to go since it cant go back. So 3^k. and we do this k times.
O(k) to maintain the stack
"""

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(i,j):
            max_gold = grid[i][j]
            start_gold = grid[i][j]
            start_visited = set()
            len_visited_cells = 0

            stack = [[(i,j), start_visited, start_gold]]

            while stack:
                node, visited, gold = stack.pop()

                for direction in directions:
                    destination = tuple(map(lambda x,y:x+y, node, direction))
                    r,c = destination

                    if 0<=r<m and 0<=c<n and (r,c) not in visited and grid[r][c] != 0:

                        new_visited = visited.copy()
                        new_visited.add(node)
                        new_gold = gold + grid[r][c]

                        if new_gold > max_gold:
                            max_gold = new_gold
                            len_visited_cells = max(len_visited_cells, len(new_visited))

                        stack.append([destination, new_visited, new_gold])
            return max_gold, len_visited_cells
        
        max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    gold, num_cells = dfs(i,j)
                    if gold > max_gold:
                        max_gold = gold
                        
                        if num_cells >= 24:
                            return max_gold
        
        return max_gold
