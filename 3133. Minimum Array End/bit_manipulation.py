"""
My solution is convoluted and there might be an easier way.
Since its AND, we need to maintain the 1 bits as is for x.
If x = 5 = 101, the 0th and 2nd bits always have to be one (right to left).
That means if n = 1, result is 5.
But if n = 2, we can only change the middle bit, and thus we get 111 = 7.
Now if n = 3, we cannot make any other changes to current bits, so we add 1 to prefix and get 1101 = 13.
If n = 4, we can again only change the 1st bit (0 indexed) and we get 1111 = 15.
Now when n = 5, we again increment the prefix to 2 and get 10101 => 10 + 101 => 2 + 5.
The pattern is that we need to see how many numbers we can increase within the same group without changing the prefix.
That depends on number of 0s in x. 5 has 1 zero and so we have 2 options for it.
If x = 4 = b100, we get 4 options, 100, 101, 110, 111. 
It basically is 2^num_zeros.
This way we can find the group and then get the index in a group.
The group is the prefix.

O(logn) time.
O(logn) space.
"""

class Solution:
    def minEnd(self, n: int, x: int) -> int:

        def bin_to_dec(bin_string):
            bin_string = bin_string[::-1]
            res = 0
            for i,c in enumerate(bin_string):
                if c == '1':
                    res += 2**i
            return res

        # get max number of variables allowed, for 5 -> 101, we can only set the middle bit to either 1 or 0.
        size = 0
        num_zeros = 0
        for c in bin(x)[2:]:
            if c == '0':
                size += 1
                num_zeros += 1
        size = 2**size
        
        # get the prefix
        prefix = (n-1) // size

        # get the remaining number, aka next within current group
        rem_idx = (n-1) % size
        rem_idx_bin = bin(rem_idx)[2:]       
        # pad with zeros if needed
        rem_idx_bin = rem_idx_bin[::-1] + ('0' * max(0, num_zeros - len(rem_idx_bin)))

        # update the 0s in x with corresponding ones in rem_idx
        i = 0
        bin_x = bin(x)[2:]
        bin_x = bin_x[::-1]
        bin_x = [c for c in bin_x]
        for idx in range(len(bin_x)):
            if bin_x[idx] == '0':
                if rem_idx_bin[i] == '1':
                    bin_x[idx] = '1'
                i += 1
        bin_x = bin_x[::-1]
        bin_x = ''.join(bin_x)

        # add prefix
        res_bin = bin(prefix)[2:] + bin_x
        return bin_to_dec(res_bin)
