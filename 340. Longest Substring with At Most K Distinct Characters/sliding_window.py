"""
Sliding window.
Expand the window with r and shrink with l.
Keep expanding, and keep the track of the frequency of all chars in current window.
If at any point len(freq.keys()) > k, we need to shrink the window.
Keep shrinking till the len(freq) > k by reducing count of a char at s[l]. If any value becomes 0, delete that key, this shrinks the freq size.
update result and shift r.

O(n) time for sliding window.
O(k) space since the freq map will at most store k keys.
"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        freq = {}
        res = 0
        l = 0
        r = 0

        while r<len(s):
            if s[r] not in freq:
                freq[s[r]] = 0
            freq[s[r]] += 1
            # fix by shifting left
            while len(freq) > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            
            res = max(res, r-l+1)
            r += 1
        
        return res
