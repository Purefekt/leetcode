class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert int to str
        x = str(x)
        
        l = 0
        r = len(x)-1
        
        while l<=r:
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1
        
        # if while loop ends without false, then it is a palinedrome
        return True
    