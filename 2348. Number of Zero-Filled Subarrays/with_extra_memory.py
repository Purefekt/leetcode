"""
If we have 1 zeros, then we have 1 subarray. If we have 2 zeros, then we have 3 subarrays, if we have 3 zeros, then we have 6 subarrays. This pattern continues.
The number of subarrays for n+1 zeros is number of subarrays for n + int(n+1).
We can find the frequency of all subarrays of zeros.
Then find the largest subarray length and get the number of subarrays for that length. This will give us all values till that array length.
Then we use the frequency of all subarrays of zeros to calculate the final result.

O(n) time
O(n) space
"""

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        # find all subarrays of zeros
        freq_subarrays = collections.defaultdict(int)
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            else:
                if cnt > 0:
                    freq_subarrays[cnt] += 1
                cnt = 0
        if cnt > 0:
            freq_subarrays[cnt] += 1
        
        if not freq_subarrays:
            return 0
        
        # calculate the number of zeros for highest freq subarray
        largest = max(freq_subarrays)

        num_zeros = {0:0}
        for i in range(1, largest+1):
            num_zeros[i] = num_zeros[i-1] + i
        
        # use the freq subarrays to get the final result
        res = 0
        for k,v in freq_subarrays.items():
            res += v * num_zeros[k]
        
        return res
