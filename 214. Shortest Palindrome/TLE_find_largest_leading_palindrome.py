"""
TLE, but good to understand.
We can find the longest palindrome which starts at index 0.
We now simply need to reverse the remaining chars at the end of this palindrom and add it to the start.
If s = aace, the longest palindrome which starts at 0 is 'aa'.
We reverse ce and add it to s to make ecaace, which is the result.

O(n^2) time to find the largest palindrome.
O(n) space.
"""

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        def is_palin(r):
            l = 0
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        # get the longest palindrome which starts at 0
        longest_palin_end_idx = -1
        for r in range(len(s)-1, -1, -1):
            if is_palin(r) is True:
                longest_palin_end_idx = r
                break
        
        to_reverse = s[longest_palin_end_idx+1:]
        
        res = to_reverse[::-1] + s
        return res
