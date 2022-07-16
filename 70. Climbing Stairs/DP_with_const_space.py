"""
Dynamic Programming. with contant space using 2 variables.

1D DP. When we draw the tree, we can see when we are at node == n, we have 1 way of reaching the end. When we are at node == n-1, we also have 1 way of reaching the end. For node == n-2, we have 2 ways of reaching the end (n+n-1) and so on. We fill out a 1D array bottom up, and the number when node==0 is the final answer.

We dont need to maintain the full array and can just use 2 variables and keep updating them
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # one if n-1, when we need 1 step from the prev step to reach the end
        # two is n, when we need 2 steps from the prev step to reach the end
        one = 1
        two = 1
        for i in range(n-1):
            one_cache = one
            one = one+two
            two = one_cache
            
        
        return one
    