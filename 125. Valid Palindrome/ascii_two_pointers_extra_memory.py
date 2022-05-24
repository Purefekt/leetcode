class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # ascii and two pointers, but using more memory since we create a new string
        new_s = ''
        
        # format the string
        for n in s:
            if self.get_alphanumeric(n) == True:
                new_s = new_s + n
        new_s = new_s.lower()
        
        # pointers part
        l = 0
        r = len(new_s) - 1
        
        while(l<r):
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1
        return True
                
        
        # helper function to get only alphanumeric string
    def get_alphanumeric(self, n):
        if ((ord(n) >= ord('A') and ord(n) <= ord('Z')) or
            (ord(n) >= ord('a') and ord(n) <= ord('z')) or
            (ord(n) >= ord('0') and ord(n) <= ord('9'))):
            return True
        return False
            