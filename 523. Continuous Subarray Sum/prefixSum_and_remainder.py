"""
Prefixsum and modulo.
Calculate the prefixsum of the array, add an extra 0 to the left end (start).
But when getting psum, dont store the psum in the array, instead store psum%k.
This is because we only care about the mod.
Doing this changes this into a simple continuous subarray sum problem where we need to sum to k.
Iterate through the mod psum array, if current value exists in hashmap, then check if it is atleast 2 spaces away.
Hashmap stores the index of the first occurance of a unique number.

O(n) time to create the psum array and another pass to determine the solution.
O(n) space used by psum array and first occurance hashmap.
"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        psum = [0]
        cur = 0
        for n in nums:
            cur += n
            psum.append(cur%k)
        
        first_occ = {}
        for i,ps in enumerate(psum):
            if ps not in first_occ:
                first_occ[ps] = i
            else:
                if i - first_occ[ps] > 1:
                    return True
        
        return False
