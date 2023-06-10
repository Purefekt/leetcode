"""
Follow up: Without converting to string
We need to compare the rightmost and leftmost values, remove and repeat
Rightmost digit is x%10
Leftmost digit is x//div, where div is a multiple of 10 with the same number of digits as x
eg: x=2112, div=1000. Rightmost -> 2112%10 = 2. Leftmost -> 2112//1000 = 2
Now remove both these digits. To remove leftmost x%div, to remove rightmost x//10
Repeat till x exists. At any point l!=r, return False

O(log_10(n)) time. Since we divide the input by 10 on each iteration.
O(1) space to store r,l and div in constant space.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x<0:
            return False
        
        # find a multiple of 10 at the same level as x
        div = 1
        while div <= x:
            div *= 10
        div //= 10
        
        # right most digit %10, left most digit //div
        while x:
            r = x%10
            l = x//div

            if r!=l:
                return False
            
            # update x, remove leftmost and rightmost digits
            # remove leftmost with %div and remove rightmost with //10
            x %= div
            x //= 10

            # update the divider by /100. Since we removed 2 digits, we dec it by 100X
            div //=100
        
        return True
        