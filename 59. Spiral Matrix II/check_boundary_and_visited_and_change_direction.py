"""
Initialize a n*n matrix with zeros so we can input numbers using index.
start from (0,0) and keep adding numbers by moving right, then down, then left, then up and then back to right.
Change direction when we hit a boundary or a visited node
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        # initialize n*n matrix with 0s
        matrix = []
        for i in range(n):
            curr_row = []
            for j in range(n):
                curr_row.append(0)
            matrix.append(curr_row)
        
        
        # add elements to the matrix
        num = 1
        visited = set()
        i,j = 0,0
        directions = {
            'right' : (0,1),
            'down' : (1,0),
            'left' : (0,-1),
            'up' : (-1,0)
        }
        curr_dir = 'right'
        
        # add (0,0) to visited and matrix
        matrix[i][j] = num
        visited.add((i,j))
        while num != n*n:
            r,c = directions[curr_dir]
            if i+r>=0 and j+c>=0 and i+r<n and j+c<n and (i+r, j+c) not in visited:
                i = i+r
                j = j+c
                num += 1
                matrix[i][j] = num
                visited.add((i,j))
            else:
                if curr_dir == 'right':
                    curr_dir = 'down'
                elif curr_dir == 'down':
                    curr_dir = 'left'
                elif curr_dir == 'left':
                    curr_dir = 'up'
                elif curr_dir == 'up':
                    curr_dir = 'right'
        
        return matrix          
            