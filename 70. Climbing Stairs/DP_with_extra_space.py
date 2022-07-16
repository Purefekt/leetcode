"""
Dynamic Programming. with extra space

1D DP. When we draw the tree, we can see when we are at node == n, we have 1 way of reaching the end. When we are at node == n-1, we also have 1 way of reaching the end. For node == n-2, we have 2 ways of reaching the end (n+n-1) and so on. We fill out a 1D array bottom up, and the number when node==0 is the final answer.

Here we use extra space since we maintain an array of size n.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        
        output = [1,1]
        for i in range(n-1):
            output.append(output[0+i] + output[1+i])
        
        return output[-1]
    