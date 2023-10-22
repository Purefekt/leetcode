"""
DP. Recursion with memo.
Create a hashmap of vowel to possible vowel mappings.
Use helper function which takes previously selected char and current index.
if (prev,idx) in cache, return.
If the idx == length, this means we have a valid combo and return 1.
iterate over all possible children of prev and add to its count.
To start, run helper with each of the 5 vowels as the starting prev and thus the starting idx is 1.

O(n) time since we call 5 vowels n times, thus 5*n.
O(n) space for the stack. 
"""

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        mod = 10**9 + 7
        opts = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }

        memo = {}
        def helper(prev, idx):
            if (prev, idx) in memo:
                return memo[(prev, idx)]

            if idx == n:
                return 1
            
            count = 0
            for op in opts[prev]:
                count += helper(op, idx+1)
            memo[(prev, idx)] = count
            return count
        
        res = 0
        for c in opts:
            res += helper(c, 1)
            res %= mod

        return res
        