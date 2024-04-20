"""
Find connected components.
For each connected component, we need to keep track of the leftmost and rightmost cells.
Leftmost cell will always have the lowest i+j value.
Rightmost cell will always have the highest i+j value.
Keep track of these 2 and update leftmost and rightmost cell coordinates.

O(m*n) time to run dfs. Each cell will be visited at most once.
O(m*n) space since max size of stack can be m*n. The visited set will also contain m*n at the end.
"""

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        m = len(land)
        n = len(land[0])

        visited = set()
        res = []
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and (i,j) not in visited:
                    # start dfs and keep track of min coordinate and max coordinate
                    min_coord_val = i+j
                    max_coord_val = i+j
                    min_coord = [i,j]
                    max_coord = [i,j]

                    stack = [(i,j)]
                    while stack:
                        node = stack.pop()
                        r,c = node
                        if node in visited:
                            continue
                        if r+c < min_coord_val:
                            min_coord_val = r+c
                            min_coord = node
                        if r+c > max_coord_val:
                            max_coord_val = r+c
                            max_coord = node

                        for d in directions:
                            dest = tuple(map(lambda x,y: x+y, node, d))
                            new_r, new_c = dest
                            if 0<=new_r<m and 0<=new_c<n and dest not in visited and land[new_r][new_c] == 1:
                                stack.append(dest)
                        
                        visited.add(node)

                    res.append([min_coord[0], min_coord[1], max_coord[0], max_coord[1]])
        
        return res
