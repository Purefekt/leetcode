"""
Get the max width for each cell in the matrix.
Iterate through each row and for each cell keep adding 1s, if we hit a 0, reset it to 0.
Now we will have a matrix with max widths for each cell.
We can calculate the max rectangle at a cell using this info by linearly searching upwards.
If we have [
    1,0,1,0,1
    1,0,1,1,1
    1,1,1,1,1
]
Then the max width matrix will be [
    1,0,1,0,1
    1,0,1,2,3
    1,2,3,4,5
]
Now if we take the bottom right most cell, we go upwards and only care about its own max width column, which is [
    1
    3
    5
]
In first iteration, we see that the max width is 5 and height is 1 and so area is 5.
In second iteration, we see that the max width is 3 and height is 2 and so area is 6.
In third iteration, we see that the max width is 1 and height is 3 and so area is 3.
Out of these we track the max area which is 6.
We repeat this for every single cell.

O(n^2*m) time since for each cell we perform this calculation for all n rows and we have n*m cells.
O(n*m) space for the matrix, though we can safely use input matrix for max width matrix and use O(1) space.
"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        # get the max width of column for each cell
        for i in range(m):
            matrix[i][0] = int(matrix[i][0])
            for j in range(1, n):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = int(matrix[i][j-1]) + 1
        
        res = 0
        for i in range(m):
            for j in range(n):
                min_width = matrix[i][j]
                res = max(res, min_width)

                # for each cell, go up and get the area of triangles using the min width
                iteration = 2
                for k in range(i-1, -1, -1):
                    min_width = min(min_width, matrix[k][j])
                    if min_width == 0:
                        break
                    res = max(res, min_width * iteration)
                    iteration += 1
        
        return res
