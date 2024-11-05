"""
Greedy.
Check every partition of 2 from start till end.
if we have 1001, we have 2 such partitions, s[0:2] and s[2:4] or 10 and 01.
If we can make these subpartitions with the same char, then we will get a beautiful string.
We dont need to worry about if a partition becomes 00 or 11, we just add how many operations done.
If both chars in a sub partition are the same, then increase 0. Else increase 1.

O(n) time for one pass over s.
O(1) space.
"""

class Solution:
    def minChanges(self, s: str) -> int:
        
        # check each pair
        res = 0
        for i in range(0, len(s), 2):
            if s[i] == s[i+1]:
                res += 0
            else:
                res += 1
        
        return res
