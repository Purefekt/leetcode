"""
Dynamic Programming
Create the dp matrix of the same size as costs.
The columns are colors R,B,G and the rows are houses.
Each cell in the dp matrix means the total min sum if we chose that color for that house.
So the last row is the min sum of painting all the houses, and the first col in that means that the min sum of painting all houses if we end with a red house.
Thus each row will be updated by taking the cost of painting that house and the min sum of painting previous houses OTHER than the color we chose for current house.

O(n) time for n houses.
O(n) space for n houses. NOTE can be optimized to O(1) space.
"""

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        dp = []
        for i in range(len(costs)):
            dp_row = []
            for j in range(3):
                dp_row.append(0)
            dp.append(dp_row)
        
        # init first row
        for j in range(3):
            dp[0][j] = costs[0][j]
        
        # for each row, the columns are Red, Blue, Green
        # a cell is the total min sum we get if we take that color in that row
        # the value at each cell will be itself + min of OTHER 2 colors in previous cell
        for i in range(1, len(costs)):
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        
        return min(dp[-1])
