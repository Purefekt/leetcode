"""
Sliding window.
When we OR numbers, it only gets larger since the bit we set, doesnt get unset again.
We use a sliding window technique to increase a window till the OR >= k.
When we hit such a window, now we need to decrease it from left side until we reach <k again.
Tricky part is to know how to un-OR numbers we remove from the list.
For this, create a hashmap to store the counts of set bits.
A hashmap of size 32 which stores the counts of all bits.
To get the current value, we can iterate over this hashmap, for any bit count >0, it is currently set and thus will be treated as 1, else 0.

O(n) time for sliding window, the calculation of current value takes O(32) or constant time.
O(1) space since hashmap is of fixed size 32.
"""

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        bit_counts = {i:0 for i in range(32)}
        l = 0
        res = math.inf
        for r in range(len(nums)):
            # add nums[r] to current window
            bin_r = bin(nums[r])[2:]
            bin_r = bin_r[::-1]
            for i,c in enumerate(bin_r):
                if c == '1':
                    bit_counts[i] += 1

            cur_val = 0
            for i in range(32):
                if bit_counts[i] > 0:
                    cur_val += 2**i
            
            while cur_val >= k and l<=r:
                res = min(res, r-l+1)
                # move l
                bin_l = bin(nums[l])[2:]
                bin_l = bin_l[::-1]
                for i,c in enumerate(bin_l):
                    if c == '1':
                        bit_counts[i] -= 1
                
                cur_val = 0
                for i in range(32):
                    if bit_counts[i] > 0:
                        cur_val += 2**i
                l += 1
            else:
                r += 1
        
        if res == math.inf:
            return -1
        return res
