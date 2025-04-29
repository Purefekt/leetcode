"""
Get the max width for each cell in each row.
For a matrix like:
[
    1,0,0,1,1
    1,0,1,1,1
    1,1,0,1,1
]
We get
[
    1,0,0,1,2
    1,0,1,2,3
    1,2,0,1,2
]
Now iterate through all cells.
For each cell, go top to bottom and see the largest height we can have.
During this process also track the min height of all the cells we are considering.
Suppose we are at [1][4], we see that the width is 3 and we set height to 1. Area is 1*3.
Now we go down and see the cell below us is also not 0, now height is 2 but the width is 2 since we depend on the smallest width. New area is 2*2.
Note that we would have had an earlier better area when we started at [0][4] 
    first we get area as 1*2
    then we get area as 2*2 
    then we get area as 3*2

O(m*m*n) since we traverse through the entire matrix and for each cell, go down all the rows.
O(m*n) space used by width matrix
"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        m,n = len(matrix), len(matrix[0])

        #get max width of each cell
        width = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            width.append(row)
        
        for i in range(m):
            cur = 0
            for j in range(n):
                if matrix[i][j] == '0':
                    cur = 0
                else:
                    cur += 1
                width[i][j] = cur
        
        # now we have the maximal width at each cell
        # we can use this to find the maximum area
        # iterate through each cell
        # for each cell, go top to bottom and get the largest height we can while still adding cells which are 1. During this track the min width 
        res = 0
        for i in range(m):
            for j in range(n):
                if width[i][j] != 0:
                    min_width = width[i][j]
                    res = max(res, min_width)

                    height = 1
                    k = i+1
                    while k<m and width[k][j] != 0:
                        height += 1
                        min_width = min(min_width, width[k][j])
                        res = max(res, min_width * height)
                        k += 1
        
        return res
