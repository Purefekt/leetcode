"""
DP.
Fill the triangle bottom up. Bottom most layer will be as it is. For each element in each layer going up, update it to be itself + the min of both its possible paths. The value at [0][0] will be the min path cost
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # fill in place bottom up from the 2nd last layer. Start filling from triangle[2][0] for the given example 1
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
        
        return triangle[0][0]
    