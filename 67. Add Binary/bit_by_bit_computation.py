class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # always keep a larger
        if len(b) > len(a):
            a,b = b,a
        
        b = "0" * (len(a)-len(b)) + b

        carry = 0
        res = ""
        for i in range(len(a)-1, -1, -1):
            val = int(a[i]) + int(b[i]) + carry
            if val == 0:
                res += '0'
                carry = 0
            elif val == 1:
                res += '1'
                carry = 0
            elif val == 2:
                res += '0'
                carry = 1
            elif val == 3:
                res += '1'
                carry = 1
        
        if carry == 1:
            res += '1'
        
        res = res[::-1]
        return res
