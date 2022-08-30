"""
Make a hashmap for all original values and 6 exceptions
go through these numbers and compare it to the input, if input is larger, append the corresponding letter to the ans X number of times which is the quotiant of num/n
subtract the input num by the amount which was added to the answer and continue
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        
        hashmap = {
            1000:'M',
            900:'CM',
            500:'D',
            400:'CD',
            100:'C',
            90:'XC',
            50:'L',
            40:'XL',
            10:'X',
            9:'IX',
            5:'V',
            4:'IV',
            1:'I'
        }
        
        keys = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        
        ans = ''
        for n in keys:
            if num >= n:
                ans += (hashmap[n]*(num//n))
                num -= (n*(num//n))
        
        return ans
        