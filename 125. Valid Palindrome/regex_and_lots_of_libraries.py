import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using regex and lots built in libraries
        
        # format the string
        s = s.lower()
        valid = r'[^a-zA-Z0-9]'        
        new_s = re.sub(pattern=valid, repl='', string=s)
        
        reverse_s = new_s[::-1]
        
        if reverse_s == new_s:
            return True
        return False