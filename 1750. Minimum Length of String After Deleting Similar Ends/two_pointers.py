"""
Two pointers.
Set left to 0 and right to len(s)-1.
If s[l] != s[r], exit.
Now s[l] == s[r] == char.
Shift left pointer till the next element is not char. Shift right pointer the same way.
Then move pointers 1 position to continue.

O(n) time to iterate over the array at max once.
O(1) space.
"""

class Solution:
    def minimumLength(self, s: str) -> int:
        
        l = 0
        r = len(s)-1

        while l<r:
            if s[l] != s[r]:
                break

            char = s[l]
            while l<r-1 and s[l+1] == char:
                l += 1
            while r>l+1 and s[r-1] == char:
                r -= 1
            l += 1
            r -= 1
        
        if l>r:
            return 0
        return r-l+1
