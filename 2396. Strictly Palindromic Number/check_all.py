"""
Check base string representation is a palindrome or not
If it is at any point, return False
"""

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        def check_palindrome(s):
            l = 0
            r = len(s)-1
            while l<=r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def find_base_rep(base):
            res = ''
            m = n
            while m>0:
                res = res + str(m%base)
                m = m//base
            return res[::-1]
        
        for base in range(2,n-1):
            string_rep = find_base_rep(base)
            if check_palindrome(string_rep) is False:
                return False
        
        return True
