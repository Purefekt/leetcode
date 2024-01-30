"""
Top down dp.
If n is 1, return 0. This is to avoid edge cases on paste operation.
Recursive function takes (copied, current), copied is currently copied frequency and current is the current number of 'A' on the screen.
If current == n, return 0.
If current > n, return inf, since this is an invalid solution.
We can either choose to copy or paste.
But we need to avoid copying the same value again and again. Suppose current value is 1 and copied is 1. If we perform copy operation, then we will again copy 1 and current stays 1, this will go on forever.
Thus set copy = inf, and only if current!=copied, add 1 and continue.
Paste can always be performed, add 1 and update current = current + copied.
Return min of copy and paste.
Add memoization.

O(n^2) time. Recursive function runs for all pairs of copied and current, each can be at max n.
O(n2^2) space for memoization table.
"""

class Solution:
    def minSteps(self, n: int) -> int:

        if n==1:
            return 0
        
        memo = {}
        def helper(copied, current):
            if (copied, current) in memo:
                return memo[(copied, current)]

            if current == n:
                memo[(copied, current)] = 0
                return 0
            
            if current > n:
                memo[(copied, current)] = math.inf
                return math.inf
            
            # only copy if allowed
            copy = math.inf
            if current != copied:
                copy = 1 + helper(current, current)
            paste = 1 + helper(copied, current+copied)

            memo[(copied, current)] = math.inf
            return min(copy, paste)
        
        return helper(1,1) + 1
        