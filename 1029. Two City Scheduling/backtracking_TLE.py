"""
Backtrack with pruning. Better brute force, TLE
Start with the first person, he can either go to A and incur Ai cost or go to B and incur Bi cost.
If this person goes to A, then number of A will be +=1, same for B is this person goes to B
Rexursive function takes total current sum, number of A, number of B and persons index
If sum of A and B is n, we have reached a base case and update the min_cost
Else if A is less than n//2, we can still go to A, same for B
"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        res = [inf]

        def backtrack(cost_sum, A, B, idx):
            if A+B == n:
                if cost_sum < res[-1]:
                    res[0] = cost_sum
                return
            
            if A<n//2:
                cost_sum += costs[idx][0]
                backtrack(cost_sum, A+1, B, idx+1)
                cost_sum -= costs[idx][0]
            
            if B<n//2:
                cost_sum += costs[idx][1]
                backtrack(cost_sum, A, B+1, idx+1)
                cost_sum -= costs[idx][1]
        

        backtrack(0,0,0,0)
        return res[0]
        