"""
Without changing to string.
if x = 12321, find multiple of 10 with the same digits, here divider = 10000
x%10 will give the right most vale
(x//divider)%10 will give the left most value
compare them, if not same, false, else repeat and set x -> x//10 and repeat
reduce divider by 100 fold on every iteration since we get rid of 2 units, leftmost and rightmost
repeat till divider is less than or eq to 1
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # false for negatives
        if x<0: return False
        
        # find divider
        divider = 1
        while x >= divider:
            divider = divider*10
        divider = int(divider/10)
        
        
        while divider > 1:
            if x%10 != (x//divider)%10:
                return False
            x = x//10
            divider = divider//100
        return True
    