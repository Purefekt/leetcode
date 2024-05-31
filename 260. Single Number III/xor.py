"""
Bit manipulation.
If we xor all nums, we get the xor of the two numbers which are singular.
This is bcos a^a = 0.
Suppose we have [1,2,1,3,2,5], if we xor all, we get 6.
Now 6 tells us exactly which bits differ at which position in the 2 numbers we are looking for.
6 = b110, this means they differ at 2nd and 3rd significant bits.
We only need 1 bit they differ at, so we can loop till 32 and get the bit where it is 1, which is the 2nd bit.
This means if the result is [a,b], then a will have 0 at ith bit and b will have 1 at ith bit.
Now we place all numbers into 2 buckets, all numbers with ith bit == 0 will go in bucket1.
All numbers with ith bit == 1 will go in bucket2.
All duplicates will automatically fall into the same bucket.
So if we iterate over nums, check the ith bit and xor into the correct bucket, the final buckets will be the solution numbers.

O(n) time to iterate over nums in 2 passes.
O(1) space.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        all_xor = 0

        for n in nums:
            all_xor ^= n
        
        # find the ith bit which differs, ie this bit will be 1
        for i in range(32):
            if all_xor & 1 == 1:
                break
            all_xor = all_xor >> 1
        
        num1 = 0
        num2 = 0
        for n in nums:
            # get the ith bit, if its 0, put it in bucket1, else put it in bucket2
            n_shift = n >> i
            if n_shift & 1 == 0:
                num1 ^= n
            else:
                num2 ^= n
        
        return [num1, num2]
