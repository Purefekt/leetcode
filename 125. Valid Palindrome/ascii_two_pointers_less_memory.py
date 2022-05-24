class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ## ascii and two pointers with less memory by not making a new string
        ## on each step, check if the character at the pointer is valid alphanumeric, if not then increment or decrement (l or r)
        
        # pointers
        l = 0
        r = len(s) - 1
        
        while(l<r):
            while l<r and self.get_alphanumeric(s[l]) == False:
                l = l + 1
            while l<r and self.get_alphanumeric(s[r]) == False:
                r = r - 1
            
            if s[l].lower() != s[r].lower():
                print(s[l], s[r])
                return False
            
            l = l + 1
            r = r - 1
        
        return True
        
    
    # helper function to check if ascii
    def get_alphanumeric(self, n):
        if (
            (ord(n) >= ord('A') and ord(n) <= ord('Z')) or
            (ord(n) >= ord('a') and ord(n) <= ord('z')) or
            (ord(n) >= ord('0') and ord(n) <= ord('9'))
        ):
            return True
        return False