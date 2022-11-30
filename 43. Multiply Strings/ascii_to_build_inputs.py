"""
Using ascii to build both nums and multiply at the end

O(max(m,n)) time. where m is the length of num1 and n is the length of num2
O(1) space
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # build first num
        number1 = 0
        factor = 1
        for i in range(len(num1)-1, -1, -1):
            number1 = number1 + (ord(num1[i]) - ord("0"))*factor
            factor *= 10
        
        # build second num
        number2 = 0
        factor = 1
        for i in range(len(num2)-1, -1, -1):
            number2 = number2 + (ord(num2[i]) - ord("0"))*factor
            factor *= 10
        
        return str(number1*number2)
             