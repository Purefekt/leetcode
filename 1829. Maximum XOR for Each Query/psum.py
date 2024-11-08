"""
Get the psum xor for the array.
psum[i] is the total xor till that index, now we need to xor it with 1 more number which should maximize the result.
We will always be able to get 2^maxbit - 1 as the maximized value.
Suppose psum[i] = 2 and maxbit = 3.
2 is b10.
If maxbit is 3, then maxint is 2^3 - 1 = 7 which is b111.
So we need to perform 2 ^ X = 7.
For this we can simply take 2 and complement it.
First pad 2 to get b010. Now we complement it and get b101.
b010 ^ b101 = b111 === 2 ^ 5 = 7.
Do this for all indexes of psum.

O(n) time to iterate through nums and perform the calculation. The calculation runs in constant time.
O(1) space since psum can just be an int.
"""

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        max_int = 2**maximumBit - 1
        max_bin = bin(max_int)[2:]
        max_bits = len(max_bin)

        def get_decimal(bin_string):
            res = 0
            bin_string = bin_string[::-1]
            for i,c in enumerate(bin_string):
                if c == '1':
                    res += 2**i
            return res

        res = []
        psum_xor = 0
        for n in nums:
            psum_xor ^= n
            # pad with needed zeros
            bin_string = bin(psum_xor)[2:]
            if len(bin_string) < max_bits:
                bin_string = '0'*(max_bits-len(bin_string)) + bin_string
            # get the complement to this
            complement = ""
            for c in bin_string:
                if c == '0':
                    complement += '1'
                else:
                    complement += '0'
            decimal_val = get_decimal(complement)
            res.append(decimal_val)
        
        return res[::-1]
