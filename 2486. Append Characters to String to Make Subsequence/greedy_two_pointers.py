"""
Greedy 2 pointers.
Set pointers for both s and t.
Increment s and t is s[s_idx] == t[t_idx],
else just increment s.
Return len(t) - t_idx, since this is the number of chars missing.

O(n) time.
O(1) space.
"""

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        s_idx = 0
        t_idx = 0

        res = 0
        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
                t_idx += 1
            else:
                s_idx += 1

        return len(t) - t_idx
