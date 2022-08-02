"""
Bit by bit computation without changing into int
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # add leading zeros to the smaller string
        if len(a) > len(b):
            num_zeros = len(a) - len(b)
            b = '0'*num_zeros + b
        elif len(b) > len(a):
            num_zeros = len(b) - len(a)
            a = '0'*num_zeros + a
        
        carry = '0'
        output = []
        for i in range(len(a)):
            op1 = a[-(i+1)]
            op2 = b[-(i+1)]
            
            if op1 == '0' and op2 == '0' and carry == '0':
                output.append('0')
            elif op1 != op2 and carry == '0':
                output.append('1')
            elif op1 == '1' and op2 == '1' and carry == '0':
                output.append('0')
                carry = '1'
            elif op1 != op2 and carry == '1':
                output.append('0')
                carry = '1'
            elif op1 == '1' and op2 == '1' and carry == '1':
                output.append('1')
                carry = '1'
            elif op1 == '0' and op2 == '0' and carry == '1':
                output.append('1')
                carry = '0'
        
        if carry == '1':
            output.append('1')
        output.reverse()
        return ''.join(output)
    