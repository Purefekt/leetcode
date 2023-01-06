"""
Backtracking with memoization
Create a memo hashmap. Init it with len(s):1, this means when the index is len(s), we have reached the end with 1 valid decoding
For each step, if s[idx] == '0', means we start with a 0, this is invalid and return 0
For each decision we add 1 or 2 chars(if we have 2 chars or more left in the string)

O(n) time
O(n) space
"""

class Solution:
    def numDecodings(self, s: str) -> int:

        # If we create a string of len(s), this means we have 1 valid way to decode.
        memo = {len(s) : 1}

        def backtrack(idx):
            # if the idx is in cache, get it. If the first char is 0, this is invalid
            if idx in memo:
                return memo[idx]
            if s[idx] == '0':
                return 0
            
            # add 1 char
            res = backtrack(idx+1)

            # add 2 chars
            if idx<len(s)-1:
                if int(s[idx:idx+2]) <= 26:
                    res += backtrack(idx + 2)
            
            memo[idx] = res
            return res
        
        return backtrack(0)
