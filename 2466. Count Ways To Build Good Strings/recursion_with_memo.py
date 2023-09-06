"""
Recursion with memoization.
We dont have to build the strings but count how many we can make.
We do need the length of the string so instead of creating a recursive function where the input is the string, it can just be its length.
Base case, if it is greater than high, then it wont contribute to the result and returns 0.
If the length of current string is >= low, this means we have atleast 1 more combination.
NOTE: each path in the tree results into a totally different string. For example if we have 00 and 11, then the left side starts with 00... and the right side start with 11.., which means there will never be repeating strings, BUT, their lengths are repeated work which can be memoized.
res will be either 0 or 1 if the current length >= 1, then add the result of adding zeros and add the result of adding ones.
Add it to memo table and return.
NOTE: mod at every return of result since it will give memory limit error.

O(high) time since we compute the memoization table for each length from low till high.
O(high) space since the table stores a value for each length from low till high. 
"""

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        mod = 10**9 + 7
        
        memo = {}

        def helper(str_len):
            if str_len in memo:
                return memo[str_len]
            if str_len > high:
                return 0
            
            res = 0
            if str_len >= low:
                res += 1
            # add zeros
            res += helper(str_len + zero)
            # add ones
            res += helper(str_len + one)

            memo[str_len] = res
            return res % mod

        
        return helper(0)
