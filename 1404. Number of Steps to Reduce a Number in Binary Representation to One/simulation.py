"""
Cannot convert s to int since it will overflow, s can be 500.
Each odd binary number has 1 in its least significant bit.
If s[-1] is 1, it is odd, add 1 to it keeping s as a string.
Else divide by 2, to do that, we shift to right.
14 = 1110 and 7 = 111. 12 = 1100 and 6 = 110.
Stop when size of s == 1.

O(n^2) time since we run add_one for half the time and we need to do it from n till size = 1.
O(n) space used for string manipulations.
"""

class Solution:
    def numSteps(self, s: str) -> int:
        
        def add_one(num):
            carry = 1
            num = [c for c in num]
            for i in range(len(num)-1, -1, -1):
                if num[i] == '1':
                    if carry == 1:
                        num[i] = '0'
                        carry = 1
                    else:
                        num[i] = num[i]
                else:
                    if carry == 1:
                        num[i] = '1'
                        carry = 0
                    else:
                        num[i] = num[i]
            if carry == 1:
                num = '1' + ''.join(num)
            else:
                num = ''.join(num)
            return num
        
        res = 0

        while len(s) > 1:
            res += 1
            # odd will have 1 in the last index, add 1 to it
            if s[-1] == '1':
                s = add_one(s)
            # else divide by 2
            else:
                s = s[:-1]
        
        return res