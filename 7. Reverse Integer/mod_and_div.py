"""
Build the reverse of an int by taking the last element using %. For every next element, first update reversed by increasing it by a factor of 10.
Do this except for the first element. So for 123, we will get 32 as reversed and 1 as original.
Check the current reversed value against INT_MAX/10 and INT_MIN/10. This is to bring them to the same order.
If the reversed value is larger or smaller than each respectively, this means by adding the last number, it will under/overflow
If reversed value is exactly the same as INT_MAX or INT_MIN, check if the original digit is > than INT_MAX's last digit or < INT_MIN's last digit using %
If so, then it will also overflow/underflow
Else update reversed and add x and return

O(log(x)). Log base 10, since we divide by 10 on each iter
O(1) space
"""

class Solution:
    def reverse(self, x: int) -> int:
        
        INT_MAX = (2**31)-1
        INT_MIN = -2**31
        
        # get x_rev except last number and x which is the first digit of x
        x_rev = 0
        while x>9 or x<-9:
            x_rev = x_rev * 10
            
            x_rev = x_rev + int(math.fmod(x,10))
            x = int(x/10)
        
        # if x_rev is greater than INT_MAX/10 or less than INT_MIN/10, it will overflow/underflow
        if x_rev > int(INT_MAX/10) or x_rev < int(INT_MIN/10): return 0
        # if x_rev is equal to INT_MAX, then if x > INT_MAX%10, it will overflow
        if x_rev == INT_MAX and x > math.fmod(INT_MAX,10): return 0
        # if r_rev is equal to INT_MIN, then if x < INT_MIN%10, it will underflow
        if x_rev == INT_MIN and x < math.fmod(INT_MIN,10): return 0
        
        # else update x_rev*10 and add x to ones place
        x_rev *= 10
        x_rev += x
        return x_rev
    