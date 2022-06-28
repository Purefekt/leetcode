"""
BFS from all 0s solution. O(m*n) time and space.
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # Use all 0s to find the distances from them to all 1s
        # Add all cells with 0s to a queue.
        # update the matrix with 0 for all 0s and inf for all 1s as initial distances.
        rows = len(mat)
        cols = len(mat[0])
        queue = collections.deque()
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    mat[i][j] = 0
                else:
                    mat[i][j] = inf
        
        # for each cell in the queue, check in all 4 directions. 
        # if a directional cell's value is more than the current cell + 1, then update that cell to cell+1 distance and also add that cell to the queue
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        while queue:
            i,j = queue.popleft()
            # all 4 directions
            for dir in directions:
                new_i = i+dir[0]
                new_j = j+dir[1]
                # check validity
                if new_i>=0 and new_j>=0 and new_i<rows and new_j<cols:
                    if mat[new_i][new_j] > mat[i][j]+1:
                        mat[new_i][new_j] = mat[i][j]+1
                        queue.append((new_i, new_j))
        
        return mat
    