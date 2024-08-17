"""
DP.
Brute force would be m^2*n since for every cell (m*n) we need to get the best previous cell to take which is another pass over all columns (m).
We can use dp to get the best value of the previous row and make that operation O(1).
Set up a result 2d matrix of size m*n.
Set the first row of result = first row of points.
Start by going over all rows starting from the 2nd row.
Set an array prev_rows with values from the above row.
Fill an array left_max, left_max[0] = prev_row[0].
left_max[i] = max(left_max[j]-1, prev_row[j]). Pick the previous value with a penalty or pick value from top with no penalty.
This array is basically the highest score we can get if we use the jth column as our chosen cell. This gives us the max value till current cell from 0 -> j.
Do the same for right_max, where we get the max value of a cell from j -> n-1 cell.
Now fill res[i][j] will be points[i][j] + max(left_max[j], right_max[j]).

O(m*n) time. m*n time taken to create res matrix. Then m*3*n time taken to fill res.
O(m*n) space used by res array.
"""

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        m = len(points)
        n = len(points[0])

        res = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(None)
            res.append(row)
        
        for j in range(n):
            res[0][j] = points[0][j]
        
        # go over all rows starting from 2nd row
        for i in range(1, m):
            prev_row = [n for n in res[i-1]]
            left_max = [0 for j in range(n)]
            right_max = [0 for j in range(n)]

            # fill left_max
            left_max[0] = prev_row[0]
            for j in range(1, n):
                left_max[j] = max(left_max[j-1]-1, prev_row[j])
            
            # fill right_max
            right_max[-1] = prev_row[-1]
            for j in range(n-2, -1, -1):
                print(j)
                right_max[j] = max(right_max[j+1]-1, prev_row[j])
            
            # fill actual cell i,j
            for j in range(0, n):
                res[i][j] = points[i][j] + max(left_max[j], right_max[j])
        
        return max(res[-1])
            