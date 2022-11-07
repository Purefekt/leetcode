"""
Dynamic Programming 1D.
Each cell in the dp array is the min cost to reach that step. Len(dp) == len(cost)+1 since we need the min cost of the top floor which is after the last step in costs.
The min cost to reach steps 0 and 1 are 0 since we can start at either
Min cost to reach every next step is the min of the cost at step-2 and dp-2 and cost at step-1 and dp-1
Solution at dp[-1]

O(n) time to iterate through all costs
O(n) space to store dp array
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [None for i in range(len(cost)+1)]
        
        # reach steps 0 and 1 with 0 cost
        dp[0], dp[1] = 0, 0
        
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        
        return dp[-1]
    