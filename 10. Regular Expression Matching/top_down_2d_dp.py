"""
2d top down dp.
Use recursive helper function which takes 2 pointers, i and j.
i is the index of s and j is the index of p.
If the next char in p (j+1) is *, then we can either repeat current char or skip it. skipping it means repeating it 0 times.
If we repeat, then (i+1, j) else (i, j+2).
First case means we repeat it thus we can repeat it more and so we keep j as is and move i pointer.
Second case means we skip repeating it and thus we move to j+2 index since we need to also skip the '*'.
Also if there is a match, we move i+1 and j+1.
A match is when 2 chars are the same OR p[j] is '.'.

O(m*n) time where m is size of s and n is size of p.
O(m*n) space to store the cache table which has all m*n pairs.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}
        def helper(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            if i >= len(s) and j >= len(p):
                memo[(i,j)] = True
                return True
            
            if j >= len(p):
                memo[(i,j)] = False
                return False
            
            # boolean for if there is a match between current chars
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # if next char is *
            if j<len(p)-1 and p[j+1] == '*':
                memo[(i,j)] = helper(i, j+2) or (match and helper(i+1, j))
                return memo[(i,j)]
            
            # if there is a match
            if match:
                memo[(i,j)] = helper(i+1, j+1)
                return memo[(i,j)]
            
            memo[(i,j)] = False
            return False
        
        return helper(0,0)
