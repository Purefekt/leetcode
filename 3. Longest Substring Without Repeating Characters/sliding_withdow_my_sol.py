"""
Sliding window. Start with l and r at 0. Move right and keep checking if the expanded substring has repeating characters.
If we expand and get a repeating character in the string, move l and r by one (this will maintain the max length of sliding window)
Continue to check
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # edge case
        if len(s) == 0:
            return 0
        
        l = 0
        r = 0
        max_len = 0
        while r < len(s):
            if self.repeating(s,l,r) == False:
                max_len = (r-l) + 1
                r += 1
            else:
                l += 1
                r += 1
        
        
        return max_len
        
    
    # find if the substring has repeating characters
    def repeating(self, s, l, r):
        count_dict = {}
        
        substring = s[l:r+1]
        for c in substring:
            if c not in count_dict.keys():
                count_dict[c] = 1
            else:
                return True
        
        return False
    