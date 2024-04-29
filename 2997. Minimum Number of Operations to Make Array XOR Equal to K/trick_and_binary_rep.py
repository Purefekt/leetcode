"""
Take the xor of 3 numbers, do this by taking xor of first 2 and then taking xor of their result and the last one.
Repeat this for 4 numbers or 5. Notice that if the number of 1s in a column of bitwise operation is even, the final bitwise xor is 0.
And if the number of 1s is off, the final bitwise xor is 1.
Now suppose the final bitwise xor of nums = 4 which is 100 in binary and k = 1 which is 001 in binary.
At the 0th place we need the 0 to be 1 and at the 2nd place we need the 1 to be 0.
Since we can change the final bit just by flipping a single bit in a column, thus we only need to flip 2 bits in this case.
Algo: get the binary rep in string format for final xor and k.
Add leading zeros to the smaller one.
Compare the bit at each index, increment diff by 1 for each different one.

O(n) time where n is the size of nums to get the initial final_xor. The binary string will always be of fixed size since we cant have more than 32 chars.
O(1) space since binary string is of fixed size.
"""

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        final_xor = 0
        for n in nums:
            final_xor ^= n
        
        bin_k = str(bin(k))[2:]
        bin_final_xor = str(bin(final_xor))[2:]            

        # add leading zeros to the smaller
        if len(bin_k) < len(bin_final_xor):
            bin_k = "0" * (len(bin_final_xor) - len(bin_k)) + bin_k
        elif len(bin_k) > len(bin_final_xor):
            bin_final_xor = "0" * (len(bin_k) - len(bin_final_xor)) + bin_final_xor

        diff = 0
        for i in range(len(bin_k)):
            if bin_k[i] != bin_final_xor[i]:
                diff += 1
        
        return diff
