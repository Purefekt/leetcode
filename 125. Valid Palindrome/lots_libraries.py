class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using lots of built in functions and extra memory by creating new string without withespaces and non alphanumeric
        new_s= ''
        for n in s:
            if n.isalnum():
                new_s = new_s + n
        
        new_s = new_s.lower()
        
        # reverse string and compare
        reverse_s = new_s[::-1]
        
        if new_s == reverse_s:
            return True
        return False