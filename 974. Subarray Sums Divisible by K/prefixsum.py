"""
Prefixsum
Create the prefixsum for the array nums.
Create a pmap with {0:1},
Go through the psum array, for each num, check if num%k is in the pmap. If it is then add that value (frequency) to count
Next increment the frequency of that num%k, if it is the first time then add it to the map with 1

O(n) time to create prefix sum and to go over it again
O(n) space to store the psum%k values in pmap hashmap
"""

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        pmap = {0:1}

        psum = []
        psum_i = 0
        for num in nums:
            psum_i += num
            psum.append(psum_i)
        
        count = 0
        for num in psum:
            if num%k in pmap:
                count += pmap[num%k]
                pmap[num%k] += 1
            else:
                pmap[num%k] = 1
        
        return count
        