"""
Sliding window.
Run for loop for right from 0 till len(s).
Keep l at 0.
Calculate current total usage.
If usage > maxCost, push l till used <= maxCost.
Update result.

O(n) time since we process each index at most twice, once when adding to the window and once when removing.
O(1) space.
"""

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        l = 0

        used = 0
        res = 0
        for r in range(len(s)):
            used += abs(ord(s[r]) - ord(t[r]))
            while used > maxCost and l<=r:
                used -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            res = max(res, r+1-l)
        
        return res
