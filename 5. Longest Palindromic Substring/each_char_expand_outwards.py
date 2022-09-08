"""
for each char, expand outwards on both sides to check for palindrome
for odd palindromes start at middle
for even palindromes, start at i,i+1
o(n^2) solution
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s)<2:
            return s
        
        res = ''
        resLen = 0
        
        for i in range(len(s)):
            
            # odd chars
            l = i
            r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                # check if this palindromic len is larger than resLen
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
            
            # even chars
            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                # check if the len of this palindrom is larger than resLen
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
        
        return res
    