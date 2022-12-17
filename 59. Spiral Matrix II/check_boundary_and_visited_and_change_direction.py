"""
Initialize a matrix of n*n with None
Start from (0,0) and go right. Keep filling the matrix starting right.
Change direction if we hit a wall or visited cell. Keep change of directions in a hashmap

O(n^2) time to traverse all cells
O(n^2) to keep track of visited
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        direction_map = {
            (0,1):(1,0),
            (1,0):(0,-1),
            (0,-1):(-1,0),
            (-1,0):(0,1)
        }

        # init the matrix
        res = []
        for i in range(n):
            res_row = []
            for j in range(n):
                res_row.append(None)
            res.append(res_row)

        r,c = 0,0
        direction = (0,1)
        visited = set()
        for i in range(1,n**2 + 1):
            res[r][c] = i
            visited.add((r,c))

            # update r and c
            r += direction[0]
            c += direction[1]

            # if out of bound or visited cell, roll back r and c, change direction, update r and c
            if r>=n or c>=n or r<0 or c<0 or (r,c) in visited:
                # roll back r and c
                r -= direction[0]
                c -= direction[1]
                # change dir
                direction = direction_map[direction]
                # update r and c
                r += direction[0]
                c += direction[1]
        
        return res
