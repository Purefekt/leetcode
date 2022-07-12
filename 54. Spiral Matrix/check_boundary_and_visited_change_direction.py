"""
Start off by moving right. If we hit a boundary or a visited cell, then change to the next direction
direction is right->bottom->left->up->right and so on
repeat till output is the size of matrix

CAN BE BETTER
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        directions = {
            'right' : (0,1),
            'bottom' : (1,0),
            'left' : (0,-1),
            'up' : (-1,0)
        }
        
        output = []
        visited = set()
        # start by going right from (0,0)
        i = 0
        j = 0
        saved_i = 0
        saved_j = 0
        visited.add((i,j))
        output.append(matrix[i][j])
        curr_dir = 'right'
        
        while len(output) != m*n:
            r,c = directions[curr_dir]   
            i = i+r
            j = j+c
            
            if i>=0 and j>=0 and i<m and j<n and (i, j) not in visited:
                visited.add((i, j))
                saved_i = i
                saved_j = j
                output.append(matrix[i][j])
                          
            else:   
                i = saved_i
                j = saved_j
                if curr_dir == 'right':
                    curr_dir = 'bottom'
                elif curr_dir == 'bottom':
                    curr_dir = 'left'
                elif curr_dir == 'left':
                    curr_dir = 'up'
                elif curr_dir == 'up':
                    curr_dir = 'right'
        
        return output
      