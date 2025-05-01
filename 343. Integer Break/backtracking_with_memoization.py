"""
DP
In one step break n into all numbers from 2 -> n. call this k.
This amount is multiplied to current amount and remaining which is n-k is left over.
Base case if remaining is 0 or 1, then return 1.
Note that loop should go at max till n, so take min(remaining+1, n) since in the first call, remaining = n and that will make it go to n+1.

O(n) time.
O(n) space.
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        
        # in one step break n into all numbers from 2 -> n, call this k
        # this amount is multiplied to current amount and remaining which is n-k is left over
        # base case if remaining is 0 or 1, then return

        dp = {}
        def helper(remaining):
            if remaining in dp:
                return dp[remaining]

            if remaining == 0 or remaining == 1:
                return 1
            
            res = 1
            for k in range(2, min(remaining+1, n)):
                cur = k * helper(remaining-k)
                res = max(res, cur)
            
            dp[remaining] = res
            return res
        
        return helper(n)
