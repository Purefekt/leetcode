class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        def isPalin(s):
            l = 0
            r = len(s)-1
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        for s in words:
            if isPalin(s) is True:
                return s

        return ""
        