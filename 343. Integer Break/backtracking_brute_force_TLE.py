"""
Backtracking brute force TLE
We start with current product as 1, Suppose we have n=4, at the root of the tree we can multiply it with 1 or 2 or 3. (we cannot multiply it with 4 since that would mean we are not breaking the integer at all)
If we multiply with 1, we are left with the integer 3 to break. If we multiply with 2, we are left with integer 2 to break and so on
The recursive function takes the current product and remaining.
Base case is if remaining == 0, add the current_prod to the array res
We iterate from 1 till (inclusive) the remaining. NOTE: we go till min(n, remaining+1) to avoid going to n itself in the very first time. Return max value from res array

O(2^n) time to explore the entire tree
O(n) space for the stack
"""

class Solution:
    def integerBreak(self, n: int) -> int:

        res = []
        def backtrack(cur_prod, remaining):

            if remaining == 0:
                res.append(cur_prod)
                return
            
            for i in range(1, min(n, remaining+1)):
                backtrack(cur_prod * i, remaining-i)
        
        backtrack(1, n)
        return max(res)
