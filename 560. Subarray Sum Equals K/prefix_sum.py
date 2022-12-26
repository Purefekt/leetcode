"""
Prefix sum
Maintain a hashmap of frequency of each prefix sum. Initiate it with 0:1, which means prefixsum of 0 occurs once since when there is no array, the sum is 0
Start a loop over all nums, for each iteration update the prefix sum.
Check if prefixsum - k is in the psum_freq hashmap, if it is then add the frequency of prefixsum-k to the count
Then either add the prefixsum to the hashmap (if it doesnt exist) with a value of 1 or increment its value by 1 (if it already exists)

O(n) time to go through all elements once
O(n) space to map n elements
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        psum_freq = {0:1}
        count = 0

        prefix_sum = 0

        for n in nums:
            prefix_sum += n

            if prefix_sum - k in psum_freq:
                count = count + psum_freq[prefix_sum - k]

            if prefix_sum not in psum_freq:
                psum_freq[prefix_sum] = 1
            else:
                psum_freq[prefix_sum] += 1
        
        return count
