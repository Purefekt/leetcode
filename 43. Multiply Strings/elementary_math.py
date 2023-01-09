"""
Use a nested loop to go over all pairs of combinations b/w each index in both nums
Initialize an array of len num1+num2, since thats the max a product can be, 99*99 is a 4 digit number
Simulate how multiplication works in real life for each i,j pair. Use % and //
Reverse array and get rid of leading zeros and convert to string

O(n*m) time, where n is len of num1 and m is len of num2 
O(m+n) space for the output array
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)
        