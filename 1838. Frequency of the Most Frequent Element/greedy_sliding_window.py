"""
Greedy sliding window
Sort the numbers to have the closest ones next to each other
create a sliding window with 2 pointers, l and r at 0. R pointer will tell us that we are trying to make all numbers in the current window same as nums[r]
Keep a track of the total sum in current window
At every point check the operations needed to make all numbers in that window equal to target val. That is target val * window length - window sum
If the operations needed are more than k, we cannot have all numbers in that window equal to target val, thus move left pointer and reduce window size, also update the total sum since it has been decreased

O(nlogn) time. O(nlogn) to sort and O(n) to move the sliding window through the nums once
O(n) space to sort
"""

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()

        l = 0
        r = 0

        # r will signify what value do we want everything in the sliding window to be
        # total will track the sum currently in the window
        max_len = 1
        total = 0
        while r<len(nums):
            target_val = nums[r]
            total += nums[r]
            r += 1
            cur_len = r-l
            
            # find ops needed to make all elements in window
            ops_needed = (target_val * cur_len) - total
            # if needed ops is larger than budget, move l pointer and decrement total by nums[l-1]
            if ops_needed > k:
                l += 1
                total -= nums[l-1]
            max_len = max(max_len, r-l)
        
        return max_len
