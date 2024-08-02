"""
Sliding window.
The window size == number of total ones in the array.
Number of swaps needed in a window are the number of zeros in a window.
To fix the circular issue, attach nums to itself and make the array 2*n times long.
Now for every window, check how many zeros are there.

O(n) time where we are actually using 2*n time.
O(n) space for creating an array 2*n long.
"""

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        num_ones = sum(nums)
        
        # append nums to itself
        nums.extend(nums)

        # for each window of size num_ones, check how many 0s are there, this is the number of swaps needed
        # get num swaps for first window
        l = 0
        r = 0
        cur = 0
        for i in range(num_ones):
            if nums[r] == 0:
                cur += 1
            r += 1
        
        res = cur

        # check for all subsequent windows
        while r<len(nums):
            if nums[l] == 0:
                cur -= 1
            if nums[r] == 0:
                cur += 1
            res = min(res, cur)
            l += 1
            r += 1
        
        return res
