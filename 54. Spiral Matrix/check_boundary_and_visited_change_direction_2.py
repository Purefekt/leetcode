"""
Check boundary and visited and change directions. Keep adding to result till m*n
Start at (0,0) and move right. If at boundary or visited, shift direction to down and so on.
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        direction_change = {
            (0,1):(1,0),
            (1,0):(0,-1),
            (0,-1):(-1,0),
            (-1,0):(0,1)
        }
        
        r,c = 0,0
        direction = (0,1) #start to right
        m = len(matrix)
        n = len(matrix[0])
        res = []
        visited = set()
        
        while len(res) < m*n:
            res.append(matrix[r][c])
            visited.add((r,c))
            r += direction[0]
            c += direction[1]
            
            if r<0 or r>=m or c<0 or c>=n or (r,c) in visited:
                # go back to a valid cell
                r -= direction[0]
                c -= direction[1]
                
                # change direction
                direction = direction_change[direction]
                
                # get the next cell
                r += direction[0]
                c += direction[1]
        
        return res
    