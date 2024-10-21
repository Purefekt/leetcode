"""
Backtracking.
Get all possible splits of s.
Pass idx and current set to the helper function. Current set holds the strings currently being used.
Stop when idx == len(s) and get the max size of current set.
Use pruning to only explore valid paths.

O(n*2^n) time since the helper function runs for 2^n time and for each we run a for loop for the size of s which is n.
O(n) space used by stack and current set.
"""

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        out = 0
        def helper(idx, cur):
            nonlocal out

            if idx == len(s):
                out = max(out, len(cur))
                return
            
            for i in range(idx, len(s)):
                this_str = s[idx:i+1]
                if this_str not in cur:
                    cur.add(this_str)
                    res = helper(i+1, cur)
                    cur.remove(this_str)
        
        helper(0, set())
        return out
        