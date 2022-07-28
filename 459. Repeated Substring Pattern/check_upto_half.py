"""
check substrings starting from the first char till the mid character of the string.
on each iteration, get a repeat factor which will be len(original_string)/len(substring)
form a new string -> substring*repeat_factor
check if this is the same as the original string, if yes then return true else increase the len of current substring
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        len_orig = len(s)
        mid = len_orig//2
        
        for i in range(mid):
            curr_substring = s[:i+1]
            repeat_factor = len_orig//(i+1)
            
            if curr_substring*repeat_factor == s:
                return True
        
        return False
    