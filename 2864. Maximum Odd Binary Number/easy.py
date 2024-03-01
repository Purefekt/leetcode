class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        num_ones = 0
        for c in s:
            if c == '1':
                num_ones += 1
        
        if num_ones == 1:
            res = ""
            for _ in range(len(s)-1):
                res += '0'
            res += '1'
            return res
        
        else:
            res = ""
            for _ in range(num_ones - 1):
                res += '1'
            for _ in range(len(s) - (num_ones)):
                res += '0'
            res += '1'
            return res
