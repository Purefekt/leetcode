"""
Two pointers.
Get the indexes and chars in a 2d array for both start and target.
Suppose start = 'L_R_', then we get [(0,'L'), (2,'R')].
Now if the size of s != t, this means we have different numbers of L and R in start and target and can never reach target, so return False.
Now for each pair in s and t, we need to compare.
First if s has L but t has R, then return False, since L and R cannot pass each other. Same with if s has R and t has L.
Now if both s and t have the same char, we need to check the index.
For L, it is only valid if the index of s is >= index of t.
And for R, it is only valid if the index of s is <= index of t.

O(n) time for 3 passes over size n.
O(n) space used by index 2d matrix.
"""

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        # get the indexes and chars for L and R
        s = []
        for i,c in enumerate(start):
            if c == 'L':
                s.append((i,'L'))
            elif c == 'R':
                s.append((i,'R'))
        
        t = []
        for i,c in enumerate(target):
            if c == 'L':
                t.append((i,'L'))
            elif c == 'R':
                t.append((i,'R'))

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i][1] != t[i][1]:
                return False
            if s[i][1] == 'L' and s[i][0] < t[i][0]:
                return False
            if s[i][1] == 'R' and s[i][0] > t[i][0]:
                return False
        
        return True
