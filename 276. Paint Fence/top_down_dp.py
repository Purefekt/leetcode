"""
Top down DP.
Recursive function takes the number of fences to paint.
If there is 1 fence, we have k different ways to paint it.
If there are 2 fences, then we have k*k different ways to paint it.
Now we can either paint the next fence a different color, in that case we have k-1 options and we are left with num-1 fences.
Or we can paint the next same as the previous, in that case we have k-1 options and we are left with num-2 fences.
Memoiz it.

O(n) time.
O(n) space for the stack.
"""

class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        memo = {}
        def helper(num):
            if num in memo:
                return memo[num]

            if num == 1:
                memo[num] = k
                return k
            
            if num == 2:
                memo[num] = k*k
                return k*k
            
            # next is different
            next_is_diff = (k-1) * helper(num-1)

            # next is same, thus next is diff than i-2
            next_is_same = (k-1) * helper(num-2)

            memo[num] = next_is_diff + next_is_same
            return next_is_diff + next_is_same

        return helper(n)
