"""
Solve with PrefixSum. O(n) time and space

go through the array and keep adding the numbers. On each iteration check if the current sum-k exists in the prefixsum hashmap. If it does then add the number of times it appears to the count.

After that add the current sum to the hashmap. If the current sum is unique then add it with count 1, else increment the count
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixsum_map = {0:1}
        count = 0
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            
            # check if sum-k appears in hashmap
            if (summ-k) in prefixsum_map.keys():
                count += prefixsum_map[summ-k]
            
            # add the current sum to hashmap
            if summ not in prefixsum_map.keys():
                prefixsum_map[summ] = 1
            else:
                prefixsum_map[summ] += 1
        
        return count
    