"""
DP 1D
Using only the required variables to make space complexity O(1)
prev_2 is the min cost till the current-2nd step
prev_1 is the min cost till the current-1st step
curr_cost is the min of prev_2+cost[i-2] and prev_1+cost[i-1]
Update prev_2, prev_1 to the next elements on each iter
O(n) time
O(1) space
"""
 
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        prev_2 = 0
        prev_1 = 0
        curr_cost = 0
        
        for i in range(2,len(cost)+1):
            curr_cost = min(prev_2+cost[i-2], prev_1+cost[i-1])
            prev_2 = prev_1
            prev_1 = curr_cost
        
        return curr_cost
        