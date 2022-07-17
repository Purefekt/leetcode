"""
Start at [0,0]. Go right till we hit the boundary or an already visited cell. Change direction to down. Repeat the same and keep changing directions in the order right,down,left,up,right...
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
          
        m = len(matrix)
        n = len(matrix[0])
        
        output = []
        direction = (0,1)
        r,c = direction[0], direction[1]
        visited = set()
        i,j = 0,0
        # start off by going right
        while len(output) < m*n:
            output.append(matrix[i][j])
            visited.add((i,j))     

            if i+r>=m or j+c>=n or i+r<0 or j+c<0 or (i+r,j+c) in visited:
                # if right, change to down
                if direction == (0,1):
                    direction = (1,0)
                # if down, change to left
                elif direction == (1,0):
                    direction = (0,-1)
                # if left, change to up
                elif direction == (0,-1):
                    direction = (-1,0)
                # if up, change to right
                elif direction == (-1,0):
                    direction = (0,1)
            r = direction[0]
            c = direction[1]
            i = i+r
            j = j+c
        
        return output
                