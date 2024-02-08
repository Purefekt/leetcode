class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        num1 = num1[::-1]
        num2 = num2[::-1]

        small, large = num1, num2
        if len(num1) > len(num2):
            small, large = large, small
        
        carry = 0
        res = ""
        for i in range(len(small)):
            val = int(small[i]) + int(large[i]) + carry
            carry = val // 10
            val %= 10
            res += str(val)
        
        for i in range(len(small), len(large)):
            val = int(large[i]) + carry
            carry = val // 10
            val %= 10
            res += str(val)
        
        if carry == 1:
            res += '1'
        
        res = res[::-1]

        return res
