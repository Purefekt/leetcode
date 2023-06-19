"""
Dp with memoization.
At first we can choose either red, blue or green.
But after that every time we will have 2 choices, if we take red, then next time we can only take blue or green.
Backtrack using index and color. Keep a memoization table.
If the subproblem is in the table, return solution.
If the index == len(costs)-1, return the value.
Else the current value will be current cost value of that house of that color + min of the next subprolem.
return this result
Run the backtracking from each of the 3 colors.
The solution will be the min of the 3 start positions.

O(n) time to go over all subproblems once.
O(n) space for stack
"""

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        memo = {}
        
        def backtrack(idx, color):

            if (idx, color) in memo:
                return memo[(idx, color)]

            if idx == len(costs)-1:
                memo[(idx, color)] = costs[idx][color]
                return memo[(idx, color)]
            
            res = costs[idx][color]
            if color == 0:
                res += min(backtrack(idx+1, 1), backtrack(idx+1, 2))
            elif color == 1:
                res += min(backtrack(idx+1, 0), backtrack(idx+1, 2))
            else:
                res += min(backtrack(idx+1, 0), backtrack(idx+1, 1))
            
            memo[(idx, color)] = res
            return res
            
        
        backtrack(0,0)
        backtrack(0,1)
        backtrack(0,2)

        return min(memo[(0,0)], memo[(0,1)], memo[(0,2)])
