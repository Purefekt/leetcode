class Solution:
    def bitwiseComplement(self, n: int) -> int:

        if n==0:
            return 1
        
        # convert int to binary string
        binary = []
        while n > 0:
            mod = n % 2
            binary.append(mod)
            n //= 2
        
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
