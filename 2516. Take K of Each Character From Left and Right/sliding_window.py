"""
Sliding window.
Find the max window we can remove which still keeps atleast k of each remaining.
Start with getting counts of the 3 chars, we can use an array [a,b,c].
Set left to 0 and iterate right.
The chars in the window are to be removed, so decrement count on right pointer.
Then adjust left till the condition is satisfied.

O(n) time to get the initial counts and then for sliding window.
O(1) space used since we use pointers for the window and counts has fixed size 3.
"""

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        counts = [0,0,0]
        for c in s:
            counts[ord(c) - ord('a')] += 1
        
        if min(counts) < k:
            return -1
        
        l = 0
        max_remove = 0
        for r in range(len(s)):
            counts[ord(s[r]) - ord('a')] -= 1
            
            while min(counts) < k and l <= r:
                counts[ord(s[l]) - ord('a')] += 1
                l += 1
            
            max_remove = max(max_remove, r-l+1)


        return len(s) - max_remove
