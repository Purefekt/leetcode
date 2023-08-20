"""
Sliding window.
For each window, get the average and increment result if >= threshold.
Instead of getting the sum of current window each time, just increment the window to the right and remove one element from the left and add to the right.

O(n) time to go over the array.
O(1) space to store cur_sum
"""

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        # get the first sliding window
        cur_sum = 0
        for i in range(k):
            cur_sum += arr[i]
        
        res = 0
        if cur_sum/k >= threshold:
            res += 1
        
        # move the window
        for i in range(k, len(arr)):
            # add the ith element and remove the i-kth element
            cur_sum += arr[i]
            cur_sum -= arr[i-k]
            if cur_sum/k >= threshold:
                res += 1
        
        return res
