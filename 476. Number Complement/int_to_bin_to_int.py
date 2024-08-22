class Solution:
    def findComplement(self, num: int) -> int:
        
        # convert int to binary string
        binary = []
        while num > 0:
            mod = num % 2
            binary.append(mod)
            num //= 2
        
        # flip all chars
        for i in range(len(binary)):
            if binary[i] == 0:
                binary[i] = 1
            else:
                binary[i] = 0

        # convert binary to int
        res = 0
        for exponent, val in enumerate(binary):
            res += (val * (2**exponent))
        
        return res
