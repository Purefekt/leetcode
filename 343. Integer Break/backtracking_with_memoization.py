"""
Backtracking with memoization
We can cache the (cur_prod, remaining) tuples in a hashmap, the cache allows us to avoid repeated computation
Recursive function takes the cur_prod and remaining
If (cur_prod, remaining) is in memo, then return it
If remaining == 0 then return cur_prod
Backtrack in the same way by going from 1 -> min(n, remaining+1). At each iteration get the max val possible. Once the iteration ends, set the value in memo hashmap and return the value

O(n^2) time. We will call the recursive function at most n times and each call will run a for loop for n time
O(n) space taken by the memo hashmap and stack
"""

class Solution:
    def integerBreak(self, n: int) -> int:

        memo = {}
        def backtrack(cur_prod, remaining):

            if (cur_prod, remaining) in memo:
                return memo[(cur_prod, remaining)]

            if remaining == 0:
                return cur_prod
            
            res = 1
            for i in range(1, min(n, remaining+1)):
                res = max(res, backtrack(cur_prod * i, remaining-i))
            memo[(cur_prod, remaining)] = res
            return res
        
        backtrack(1, n)
        return  memo[(1,n)]
